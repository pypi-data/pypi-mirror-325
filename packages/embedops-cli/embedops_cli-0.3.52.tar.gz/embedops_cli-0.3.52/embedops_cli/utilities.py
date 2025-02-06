"""
`embedops_cli.utilities`
=======================================================================
miscellaneous utility functions for parsing and handling build logs
* Author(s): Bryan Siepert
"""
from os import getenv
from re import compile as re_compile
import platform
import logging
import sys
import click
import requests as requests_module
import certifi
from embedops_cli.eo_types import EmbedOpsException
from embedops_cli.config import settings
from embedops_cli.api.api_client import ApiClient
from embedops_cli.api.configuration import Configuration
from embedops_cli.api.api.default_api import DefaultApi
from . import version

_logger = logging.getLogger(__name__)

compiler_image_regex = re_compile(
    r"^registry\.embedops\.com\/dojofive\/build-images\/"
    r"(?P<compiler>[^\/\:]+)(?:\:(?P<image_version>[^\/]+))?\/?$"
)

# persistent client session to be used throughout the project
requests = requests_module.Session()

"""
The following avoids possible SSL verification errors with domains that CLI makes request against.
Some users have Root certificates that do not include the necessary certificates for SSL
    verification to work.
This fix does the following:
- Makes a HEAD request to the domains of interest. This minimizes payload and request time
- Forces the use of the Root certificate packaged with certifi
- After successful request, the Session persists the successful verification,
    so there is no need to specify certifi's Root Certicate for future requests
"""
requests.head(f"{settings.host}", verify=certifi.where())
requests.head(f"{settings.base_url}", verify=certifi.where())


def logging_setup(logger_name, level=None):
    """helper function for supporting EMBEDOPS_DEBUG_LEVEL
    environment variable-based logging controls across
    embedops_cli package

    Args:
        logger_name (_type_): the name of the module
                              e.g. __name__

    Raises:
        Exception:

    Returns:
        _type_: logging.Logger
    """
    logger = logging.getLogger(logger_name)
    if level:
        setattr(settings, "debug_level", level)
    if hasattr(settings, "debug_level"):
        if settings.debug_level not in [
            "DEBUG",
            "INFO",
            "WARN",
            "WARNING",
            "CRITICAL",
            "ERROR",
        ]:
            raise EmbedOpsException(
                message=f"EMBEDOPS_DEBUG_LEVEL '{settings.debug_level}' not supported",
                fix_message="Must be one of: DEBUG, INFO, WARN, WARNING, CRITICAL, ERROR",
            )
        logging.basicConfig()
        logger.setLevel(settings.debug_level)
        logger.debug(f"debug level set to: {settings.debug_level}")
    return logger


def get_compiler():
    """Return the name of the compiler used to generate the build log from either
    `EMBEDOPS_COMPILER`. If that environment variable is not set, we'll try to parse the compiler
    name from the `<CI_IMAGE_NAME_PLACEHOLDER>`"""
    compiler = getenv("EMBEDOPS_COMPILER", default=None)
    if compiler is None:
        _logger.warning("EMBEDOPS_COMPILER was not set. Checking for CI_REGISTRY_IMAGE")
        # fetch compiler from container name, else None
        image_registry_url = getenv("CI_REGISTRY_IMAGE", default=None)
        if image_registry_url is None:
            _logger.error("CI_REGISTRY_IMAGE could not be found")
            sys.exit(1)
        image_match = compiler_image_regex.match(image_registry_url)
        if image_match is None:
            _logger.error(
                f"The Docker image URL provided in {compiler} is not a valid image registry URL"
            )
            sys.exit(1)

        compiler_image = image_match["compiler"].upper()
        image_version = image_match["image_version"].upper()
        _logger.info(
            f"Found compiler image: {compiler_image} image version: {image_version}"
        )
        if "TI" in compiler_image:
            compiler = "TI"
        elif "GCC" in compiler_image:
            compiler = "GCC"
        elif "IAR" in compiler_image:
            compiler = "IAR"
        else:
            _logger.error(f"Compiler {compiler_image} not recognised")
            sys.exit(1)
    return compiler


def post_dict(
    endpoint_uri, data_dict=None, file_dict=None, json_dict=None, headers=None
):
    """POSTs the given object to the given URL as JSON"""

    req = requests_module.Request(
        "POST",
        endpoint_uri,
        headers=headers,
        files=file_dict,
        json=json_dict,
        data=data_dict,
    )
    prepared = req.prepare()
    session = requests_module.Session()

    return session.send(prepared, verify=certifi.where())


def quote_str_for_platform(str_to_quote):
    """Properly quote a string of command line arguments for the current platform"""
    if platform.system() == "Windows":
        # Proper quoting for cmd.exe
        #   The entire argument inside double quotes to be taken literally, except
        #   for double quotes inside the string literal, which must be escaped.
        # To accomplish this, we replace all instances of '"' with '\"'.
        #   Note: '\' must be used to escape itself in the replace pattern.
        str_to_quote = str_to_quote.replace('"', '\\"')
        return f'"{str_to_quote}"'

    # Proper quoting for Bash/zsh/etc.
    #   The entire argument inside single quotes to be taken literally.
    return f"'{str_to_quote}'"


def echo_error_and_fix(exc: EmbedOpsException):
    """Print the error message and fix messages on exceptions"""
    # Make sure we start on a newline

    version_string = f"EmbedOps CLI Version {version.__version__}"
    dashed_version_string = f"{'-' * 25} {version_string} {'-' * 25}"
    click.echo("\n")
    click.secho(f"{dashed_version_string}\n", fg="bright_red")
    click.secho(exc.message, err=True, fg="bright_red")
    click.secho(exc.fix_message, err=True, fg="white")
    click.secho("-" * len(dashed_version_string) + "\n", fg="bright_red")
    sys.exit(1)


def get_client():
    """Main method for creating a DefaultApi object for
    EmbedOps platform communication.

    Returns:
        _type_: DefaultApi
    """
    api_host = settings.get("host")
    api_key = settings.get("api_repo_key", None)

    configuration = Configuration()
    configuration.api_key["X-API-Key"] = api_key
    configuration.host = f"{api_host}/api/v1"
    api_client = ApiClient(configuration=configuration)

    return DefaultApi(api_client=api_client)
