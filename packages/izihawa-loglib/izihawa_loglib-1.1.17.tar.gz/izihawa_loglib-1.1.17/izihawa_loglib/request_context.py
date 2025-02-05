import logging
from typing import Any

from izihawa_loglib import error_log
from izihawa_utils.random import generate_request_id


class RequestContext:
    request_id_length: int = 12

    def __init__(
        self, **kwargs: Any,
    ):
        self.default_fields = kwargs
        if not self.default_fields.get("request_id"):
            self.default_fields["request_id"] = RequestContext.generate_request_id(
                self.request_id_length
            )

    def __getattr__(self, name: str) -> Any:
        try:
            return self.default_fields[name]
        except KeyError:
            classname = type(self).__name__
            msg = f'{classname!r} object has no attribute {name!r}'
            raise AttributeError(msg)

    @staticmethod
    def generate_request_id(length):
        return generate_request_id(length)

    def add_default_fields(self, **fields: Any) -> None:
        self.default_fields.update(fields)

    def statbox(self, **kwargs: Any) -> None:
        logging.getLogger("statbox").info(msg={**self.default_fields, **kwargs})

    def user_log(self, **kwargs: Any) -> None:
        logging.getLogger("user").info(msg={**self.default_fields, **kwargs})

    def debug_log(self, **kwargs: Any) -> None:
        logging.getLogger("debug").debug(msg={**self.default_fields, **kwargs})

    def error_log(self, e, level=logging.ERROR, **fields) -> None:
        all_fields = {**self.default_fields, **fields}
        error_log(e, level=level, **all_fields)

    def to_default_headers(self) -> dict[str, Any]:
        headers = {}
        if request_id := self.default_fields.get("request_id"):
            headers["X-Request-Id"] = request_id
        if client_id := self.default_fields.get("client_id"):
            headers["X-Client-Id"] = client_id
        return headers
