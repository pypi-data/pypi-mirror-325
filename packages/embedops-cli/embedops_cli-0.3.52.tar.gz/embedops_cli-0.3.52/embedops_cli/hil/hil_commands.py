"""
Contains functions for the HIL sub-group commands.
"""
import os
import json
import click
from embedops_cli.eo_types import (
    NetworkException,
    LoginFailureException,
    UnauthorizedUserException,
    HILGatewayDeviceLimitExceededException,
)
from embedops_cli.api.rest import ApiException
from embedops_cli.hil.hil_types import (
    HILRepoId404Exception,
    HILImageConfigException,
)
from embedops_cli.sse.sse_api import SSEApi
from embedops_cli.sse import eo_sse
from embedops_cli.utilities import echo_error_and_fix, requests
from embedops_cli import config
from embedops_cli.hil.hil_common import HIL_GATEWAY_IMAGE_NAME
from embedops_cli.hil.image_utility import write_image_config
from embedops_cli.hil.hil_common import hil_run, validate_verbosity
from embedops_cli import embedops_authorization
from embedops_cli.embedops_cli_internal import _handle_network_exception


@click.command()
@click.pass_context
def blink(ctx: click.Context):
    """Get a streaming response for the given event feed using urllib3."""
    try:
        sse_api = SSEApi()
        for event in sse_api.sse_blink_gateway(
            config.get_repo_id(), ctx.obj["devices"]
        ):
            if event.event == eo_sse.SSE_TEXT_EVENT:
                eo_sse.sse_print_command_text(event)
            elif event.event == eo_sse.SSE_RESULT_EVENT:
                result_event_obj = json.loads(event.data)
                ctx.exit(result_event_obj["exitCode"])
            else:
                pass  # Just ignore

        # If the command hasn't returned anything yet, exit here
        # TODO: find useful echo_eerror_and_fix to put here
        ctx.exit(1)
    except NetworkException as exc:
        _handle_network_exception(exc)


@click.command()
@click.option(
    "-v",
    "--verbosity",
    help="Log verbosity level (one of [error, warning, info, debug])",
    required=False,
    expose_value=True,
    callback=validate_verbosity,
    default="info",
)
@click.option(
    "-m",
    "--marker",
    help=(
        "Marker that will restrict which tests are run to only"
        "tests marked with @pytest.mark.<marker>"
    ),
    required=False,
    expose_value=True,
    default=None,
)
@click.argument("test_targets", nargs=-1)
@click.pass_context
def run(ctx: click.Context, test_targets, verbosity, marker):
    """Run hil in local mode, using the current repository as a source.
    Test targets are the directories, modules, or node IDs to run.
    If test targets are omitted, all tests will be run."""
    test_targets = list(test_targets)  # Convert tuple to list
    ctx.exit(
        hil_run(
            test_targets=test_targets,
            verbosity=verbosity,
            marker=marker,
            local=True,
            devices=ctx.obj["devices"],
        )
    )


def get_repo_fleet_devices():
    """Helper function that simplifies retrieving
    list of devices in fleet.

    Raises:
        NoRepoIdException: _description_

    Returns:
        list(dict()): list of device dictionaries
                      containing device id, name
                      and online status
    """
    repo_id = config.get_repo_id()

    api_client = embedops_authorization.get_user_client()
    return api_client.get_repo_fleet_devices(repo_id)


@click.command()
def fleet():
    """Get a list of fleet devices for the current repo."""

    try:
        fleet_devices = get_repo_fleet_devices()

        if len(fleet_devices) == 0:
            click.echo("No devices found in fleet.")
            return

        max_name_length = max(len(device.device_name) for device in fleet_devices)

        for device in fleet_devices:
            if device.is_online:
                status = click.style("Online", fg="green")
            else:
                status = click.style("Offline", fg="red")

            click.echo(f"{device.device_name.ljust(max_name_length)}\t{status}")

    except ApiException as exc:
        _handle_network_exception(exc)


def _check_provisioning_boundaries(api_client, repo_id):
    try:
        api_client.check_provision_limit(repo_id)
    except ApiException as exc:
        if exc.status == 401:
            echo_error_and_fix(LoginFailureException())
        elif exc.status == 403:
            echo_error_and_fix(HILGatewayDeviceLimitExceededException())
        elif exc.status == 404:
            echo_error_and_fix(HILRepoId404Exception())
        else:
            echo_error_and_fix(NetworkException(exc.status))


@click.command()
def provision():
    """Provision a new device by creating a new OS image that can
    be flashed with an external utility. The new image
    is created in the current directory, named gateway-image.img."""

    try:
        repo_id = config.get_repo_id()

        api_client = embedops_authorization.get_user_client()
        if not embedops_authorization.check_token():
            raise UnauthorizedUserException()

        _check_provisioning_boundaries(api_client, repo_id)

        url_data = api_client.get_latest_gateway_image_url()
        latest_image_url = url_data.url

        try:
            os.remove(HIL_GATEWAY_IMAGE_NAME)
        except FileNotFoundError:
            pass

        click.secho("Downloading latest gateway image...")
        with open(HIL_GATEWAY_IMAGE_NAME, "wb") as out_file:
            download_response = requests.get(latest_image_url, stream=True, timeout=300)

            if not download_response.ok:
                raise ApiException(download_response.status_code)

            out_file.write(download_response.content)

        click.secho("Provisioning device...")

        provision_data = api_client.hil_provision_device(repo_id)

        device_config_string = provision_data.device_config

        if not write_image_config(HIL_GATEWAY_IMAGE_NAME, device_config_string):
            raise HILImageConfigException()

        click.secho(
            f"{provision_data.device_name} has been provisioned. "
            f"Please complete provisioning by flashing {HIL_GATEWAY_IMAGE_NAME}"
            f" to an SD card. We recommend using either Balena Etcher"
            f" (https://github.com/balena-io/etcher)"
            f" or Raspberry Pi Imager"
            f" (https://github.com/raspberrypi/rpi-imager).\n"
        )

    except (
        NetworkException,
        UnauthorizedUserException,
        HILImageConfigException,
    ) as exc:
        echo_error_and_fix(exc)
    except ApiException as exc:
        if exc.status == 401:
            echo_error_and_fix(LoginFailureException())
        elif exc.status == 404:
            echo_error_and_fix(HILRepoId404Exception())
        else:
            echo_error_and_fix(NetworkException(exc.status))
