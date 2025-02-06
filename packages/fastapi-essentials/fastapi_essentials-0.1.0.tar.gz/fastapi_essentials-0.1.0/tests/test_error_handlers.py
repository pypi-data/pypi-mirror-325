from .types import CreateClientFixture
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi_essentials.error_handlers import (
    request_validation_error_handler,
    http_error_handler,
)
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.exceptions import RequestValidationError
from pyttp import HttpError

ENDPOINT = "/"


class Body(BaseModel):
    field: str


def test_request_validation_error_sends_4xx(create_client: CreateClientFixture) -> None:
    def create_routes(app: FastAPI) -> None:
        @app.exception_handler(RequestValidationError)
        async def _eh(request: Request, exc: RequestValidationError) -> JSONResponse:
            return await request_validation_error_handler(request, exc)

        @app.post(ENDPOINT)
        def route(body: Body) -> str:
            return "SUCCESS"

    client = create_client(create_routes)
    res = client.post(ENDPOINT, json={})
    assert res.status_code >= 400


def test_http_error_handler_returns_correct_details(
    create_client: CreateClientFixture,
) -> None:
    MSG, CODE = "msg", 404
    err = HttpError(MSG, CODE)

    def init_app(app: FastAPI) -> None:
        @app.exception_handler(HttpError)
        async def _eh(request: Request, exc: HttpError) -> JSONResponse:
            return await http_error_handler(request, exc)

        @app.get(ENDPOINT)
        def route() -> str:
            raise err
            return ""

    client = create_client(init_app)
    res = client.get(ENDPOINT)
    assert res.status_code == CODE
    assert res.json()["detail"] == err.message
