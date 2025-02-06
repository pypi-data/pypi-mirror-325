from asgi_correlation_id import CorrelationIdMiddleware
from fastapi import FastAPI
from .logging import configure_logging
from .middleware import HelmetHeaders


class Unk:
    """Make a FastAPI app an `Unk` service.

    ```python
        from fastapi_essentials import Unk
        from fastapi import FastAPI

        app = FastAPI(on_startup=[Unk.on_startup])

        Unk(app)
    ```
    """

    def __init_middleware(self, app: FastAPI) -> None:
        """init `Unk` middleware"""
        # adds requestId to logs.
        app.add_middleware(CorrelationIdMiddleware)

        app.add_middleware(HelmetHeaders)

    def __init__(self, app: FastAPI) -> None:
        """Configures common `fastapi` application functionality.

        Call this function in your main `fastify` app entrypoint,
        providing the app instance, and it will add common functionality
        to the server, like middlewares, response headers, etc.

        Example:

            ```python
            from fastapi import FastAPI

            app = FastAPI()

            Unk(app)

            # ... more code here
            ```

        Args:
            app (FastAPI): The `FastAPI` instance.

        Returns:
            None
        """
        configure_logging()
        self.__init_middleware(app)
