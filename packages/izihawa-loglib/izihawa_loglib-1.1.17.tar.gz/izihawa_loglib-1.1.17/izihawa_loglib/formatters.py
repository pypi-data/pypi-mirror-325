import dataclasses
import datetime
import logging
import os
import pprint
import time
import traceback
import typing

import orjson as json
from izihawa_utils.exceptions import BaseError

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"


class BaseFormatter(logging.Formatter):
    def _prepare(self, record):
        if isinstance(record.msg, BaseError):
            d = record.msg.as_internal_dict()
        elif isinstance(record.msg, typing.Dict) or dataclasses.is_dataclass(
            record.msg
        ):
            d = record.msg
        else:
            d = dict(message=super().format(record))

        client_ip = getattr(record, "client_ip", None)
        if client_ip:
            d["client_ip"] = str(client_ip)

        return d

    def format(self, record):
        log_record = self._prepare(record)
        return json.dumps(log_record).decode()


class DefaultHttpFormatter(BaseFormatter):
    def _prepare(self, record):
        log_record = super()._prepare(record)

        timestamp = time.time()
        formatted_datetime = datetime.datetime.fromtimestamp(timestamp).strftime(
            DATETIME_FORMAT
        )
        request_id = getattr(record, "request_id", None)
        method = getattr(record, "method", None)
        path = getattr(record, "path", None)

        log_record.update(
            unixtime=int(timestamp),
            timestamp=int(timestamp * 1_000_000),
            datetime=formatted_datetime,
            process=os.getpid(),
        )

        if request_id:
            log_record["request_id"] = request_id
        if method:
            log_record["method"] = method
        if path:
            log_record["path"] = path

        return log_record

    def format(self, record):
        log_record = self._prepare(record)
        return json.dumps(log_record).decode()


class DefaultFormatter(BaseFormatter):
    def _prepare(self, record):
        log_record = super()._prepare(record)

        timestamp = time.time()
        formatted_datetime = datetime.datetime.fromtimestamp(timestamp).strftime(
            DATETIME_FORMAT
        )

        log_record.update(
            unixtime=int(timestamp),
            timestamp=int(timestamp * 1_000_000),
            datetime=formatted_datetime,
            process=os.getpid(),
        )
        return log_record

    def format(self, record):
        log_record = self._prepare(record)
        return json.dumps(log_record).decode()


class TracebackFormatter(DefaultFormatter):
    def format(self, record):
        log_record = self._prepare(record)
        if traceback.sys.exc_info()[0] is not None:
            value = pprint.pformat(log_record, indent=2)
            value += "\n" + traceback.format_exc()
        else:
            value = json.dumps(log_record).decode()
        return value


default_formatter = DefaultFormatter()
default_traceback_formatter = TracebackFormatter()
