from logging import LogRecord
from logging.config import dictConfig
from asgi_correlation_id import CorrelationIdFilter
from asgi_correlation_id.context import correlation_id
from typing import override


class RequestIdFilter(CorrelationIdFilter):
    @override
    def filter(self, record: LogRecord) -> bool:
        """Add a `requestId` field to the `LogRecord`."""
        id_ = correlation_id.get(self.default_value)
        if id_:
            id_ = id_[: self.uuid_length]
        record.requestId = id_
        return True


def configure_logging() -> None:
    """Application logging configuration"""
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "filters": {
                "requestId": {
                    "()": RequestIdFilter,
                    "uuid_length": 8,
                    "default_value": "-",
                }
            },
            "formatters": {
                "json": {
                    "()": "pythonjsonlogger.json.JsonFormatter",
                    "format": "%(levelname)s: \t  %(asctime)s %(name)s:%(lineno)d [%(requestId)s] %(message)s",
                }
            },
            "handlers": {
                "requestId": {
                    "class": "logging.StreamHandler",
                    "formatter": "json",
                    "filters": ["requestId"],
                    "stream": "ext://sys.stdout",
                },
            },
            "loggers": {
                "root": {
                    "handlers": ["requestId"],
                    "level": "DEBUG",
                    "propagate": False,
                },
            },
        }
    )
