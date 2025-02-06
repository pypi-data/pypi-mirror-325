from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from pyttp import HttpStatus, HttpError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


async def request_validation_error_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    """A request validation error handler function.

    This is the error handler called when request validaton
    fails for a route. For example, when the parsed request body
    is invalid. This error handler acts the same as the built-in
    `request_validation_exception_handler` of `FastAPI`, but returns
    a `400` status code instead of a `422`.
    """
    return JSONResponse(
        status_code=HttpStatus.BAD_REQUEST,
        content={"detail": jsonable_encoder(exc.errors())},
    )


async def http_error_handler(request: Request, exc: HttpError) -> JSONResponse:
    """An `HttpError` error handler executed when an `HttpError` is raised within
    `fastapi` routes. Even though this handler is configured by `init_app`, it is preferred to
    use fastify's own `HttpException` when possible."""
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})
