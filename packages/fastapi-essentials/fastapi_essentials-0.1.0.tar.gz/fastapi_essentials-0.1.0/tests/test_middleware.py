from fastapi_essentials.middleware import HelmetHeaders
import pytest
from fastapi.testclient import TestClient
from .types import CreateClientFixture
from fastapi import FastAPI
from typing import Any, Callable

ENDPOINT = "/middleware"


@pytest.fixture
def client_with_middleware(
    create_client: CreateClientFixture,
) -> Callable[[Any], TestClient]:
    def _create(m: Any) -> TestClient:
        def routes(app: FastAPI) -> None:
            app.add_middleware(m)

            @app.get(ENDPOINT)
            def route() -> str:
                return "done!"

        return create_client(routes)

    return _create


class TestHelmetHeaders:
    SHOULD_HAVE_HEADERS = [
        "Content-Security-Policy",
        "Cross-Origin-Opener-Policy",
        "Cross-Origin-Resource-Policy",
        "Origin-Agent-Cluster",
        "Referrer-Policy",
        "Strict-Transport-Security",
        "X-Content-Type-Options",
        "X-DNS-Prefetch-Control",
        "X-Download-Options",
        "X-Frame-Options",
        "X-Permitted-Cross-Domain-Policies",
        "X-XSS-Protection",
    ]

    def test_get_headers(self) -> None:
        helmet_headers = HelmetHeaders.get_headers()

        has_keys = set(helmet_headers.keys())
        assert all([isinstance(x, str) for x in has_keys])
        assert all([isinstance(x, str) and bool(x) for x in helmet_headers.values()])

        assert all([h in has_keys for h in self.SHOULD_HAVE_HEADERS])

    def test_response_headers_are_set(
        self, client_with_middleware: Callable[[Any], TestClient]
    ) -> None:
        client = client_with_middleware(HelmetHeaders)
        response = client.get(ENDPOINT)

        # case-insensitive assertion
        response_header_keys = list(map(lambda x: x.lower(), response.headers.keys()))
        assert all(
            [h.lower() in response_header_keys for h in self.SHOULD_HAVE_HEADERS]
        )

        assert all(
            [
                bool(x)
                for x in response.headers.values()
                if x in self.SHOULD_HAVE_HEADERS
            ]
        )
