from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from typing import Callable, Awaitable


class HelmetHeaders(BaseHTTPMiddleware):
    """Adds response headers important for security"""

    @staticmethod
    def get_headers() -> dict[str, str]:
        """Returns a dictionary of important HTTP security headers to make `fastapi` applications more safe."""
        return {
            "Content-Security-Policy": ";".join(
                [
                    "default-src 'self'",
                    "base-uri 'self'",
                    "font-src 'self' https: data:",
                    "form-action 'self'",
                    "frame-ancestors 'self'",
                    "img-src 'self' data:",
                    "object-src 'none'",
                    "script-src 'self'",
                    "script-src-attr 'none'",
                    "style-src 'self' https: 'unsafe-inline'",
                    "upgrade-insecure-requests",
                ]
            ),
            "Cross-Origin-Opener-Policy": "same-origin",
            "Cross-Origin-Resource-Policy": "same-origin",
            "Origin-Agent-Cluster": "?1",
            "Referrer-Policy": "no-referrer",
            "Strict-Transport-Security": "max-age=15552000; includeSubDomains",
            "X-Content-Type-Options": "nosniff",
            "X-DNS-Prefetch-Control": "off",
            "X-Download-Options": "noopen",
            "X-Frame-Options": "SAMEORIGIN",
            "X-Permitted-Cross-Domain-Policies": "none",
            "X-XSS-Protection": "0",
        }

    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        response = await call_next(request)
        response.headers.update(self.get_headers())
        return response
