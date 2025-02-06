import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from typing import Callable, Generator
from .types import CreateClientFixture
from pytest_mock import MockerFixture


@pytest.fixture
def fastapi() -> FastAPI:
    return FastAPI()


@pytest.fixture
def create_client(fastapi: FastAPI) -> CreateClientFixture:
    def _create(cb: Callable[[FastAPI], None]) -> TestClient:
        app = fastapi
        cb(app)
        return TestClient(app)

    return _create


@pytest.fixture(scope="function")
def restore_mocks(mock: MockerFixture) -> Generator[None, None, None]:
    yield
    mock.resetall()
