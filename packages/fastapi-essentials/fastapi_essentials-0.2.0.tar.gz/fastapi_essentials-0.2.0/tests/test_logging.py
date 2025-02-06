from logging import getLogger
from .types import CreateClientFixture
from typing import Callable
from fastapi_essentials.logging import configure_logging
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import CaptureFixture
from json import loads
import pytest


ENDPOINT = "/logging"


def __create_route(app: FastAPI, msg: str) -> None:
    log = getLogger()

    @app.get(ENDPOINT)
    async def route() -> str:
        log.info(msg)
        return "done!"


def get_log(capsys: CaptureFixture[str], msg: str) -> str:
    captured = capsys.readouterr().out
    lines = captured.splitlines()
    line: list[str] = [
        _ for _ in lines if '"name": "root"' in _ and f'"message": "{msg}"' in _
    ]
    assert line, (
        f"Could not find log with message {msg}, are you sure you called `configure_logging()?"
    )
    return line[0]


@pytest.fixture(scope="function")
def init_client(create_client: CreateClientFixture) -> Callable[[str], TestClient]:
    def _init(msg: str) -> TestClient:
        return create_client(lambda app: __create_route(app, msg))

    return _init


@pytest.fixture()
def init_client_and_get_log(
    capsys: CaptureFixture[str], create_client: CreateClientFixture
) -> Callable[[str], str]:
    def _init(msg: str) -> str:
        client = create_client(lambda app: __create_route(app, msg))
        client.get(ENDPOINT)
        return get_log(capsys, msg)

    return _init


def test_logs_to_stdout(init_client_and_get_log: Callable[[str], str]) -> None:
    configure_logging()
    msg = "LOG"
    init_client_and_get_log(msg)


def assert_log_is_valid_json(init_client_and_get_log: Callable[[str], str]) -> None:
    configure_logging()
    msg = "LOG2"
    log = init_client_and_get_log(msg)
    assert isinstance(loads(log), dict)


def assert_request_id_in_log(init_client_and_get_log: Callable[[str], str]) -> None:
    configure_logging()
    log = loads(init_client_and_get_log("test"))
    assert "requestId" in log
