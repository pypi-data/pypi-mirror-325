"""
`telemetry`
=======================================================================
Utility for telemetry
* Author(s): Jimmy Gomez
"""
import logging
from requests import (
    ConnectionError as RequestsConnectionError,
    Timeout as RequestsTimeout,
)
from embedops_cli.config import settings
from .utilities import requests
from .embedops_authorization import get_auth_token


_logger = logging.getLogger(__name__)
measurement_id = settings.get("measurement_id")
api_secret = settings.get("api_secret")
CLIENT_ID = "embedops-cli"


def login_event():
    """Login Event"""
    event = {"name": "login"}
    send_telemetry(event)


def logout_event():
    """Logout Event"""
    event = {"name": "logout"}
    send_telemetry(event)


def command_event(command, subcommands):
    """Format CLI command event for telemetry and send"""
    event = {"name": command, "params": subcommands}
    send_telemetry(event)


def send_telemetry(event):
    """Sends telemetry to Embedops telemetry endpoint"""
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    host = settings.get("host")
    url = f"{host}/api/v1/users/myself/cli-telemetry"

    try:
        requests.post(url, headers=headers, json=event, timeout=5.0)
    except RequestsConnectionError as exc:
        _logger.debug(f"telemetry connection error: {exc}")
    except RequestsTimeout as exc:
        _logger.debug(f"telemetry timeout error: {exc}")
