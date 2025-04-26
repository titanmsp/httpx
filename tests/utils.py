import contextlib
import logging
import os
import typing

from httpx import _utils


@contextlib.contextmanager
def override_log_level(log_level: str) -> typing.Iterator[None]:
    os.environ["HTTPX_LOG_LEVEL"] = log_level

    # Force a reload on the logging handlers
    _utils._LOGGER_INITIALIZED = False
    _utils.get_logger("httpx")

    try:
        yield
    finally:
        # Reset the logger so we don't have verbose output in all unit tests
        logging.getLogger("httpx").handlers = []
