from pytest_mock import MockerFixture
from fastapi import FastAPI
from fastapi_essentials import Unk
from fastapi_essentials.middleware import HelmetHeaders
from asgi_correlation_id import CorrelationIdMiddleware


class TestUnk:
    def test_init_configures_logging(self, mocker: MockerFixture) -> None:
        import fastapi_essentials.main as main

        spy = mocker.spy(main, "configure_logging")
        app = FastAPI()
        main.Unk(app)
        spy.assert_called_once()

    def test_init_configures_middleware(self, mocker: MockerFixture) -> None:
        MIDDLEWARES_TO_CONFIGURE = [CorrelationIdMiddleware, HelmetHeaders]
        app = FastAPI()
        spy = mocker.spy(app, "add_middleware")
        Unk(app)
        spy.assert_has_calls([mocker.call(m) for m in MIDDLEWARES_TO_CONFIGURE], True)
