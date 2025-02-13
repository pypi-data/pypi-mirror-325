from __future__ import annotations

from copy import copy
import logging
import colorlog
from app.config import config as app_config
import os


class CustomFormatter(colorlog.ColoredFormatter):
    def formatMessage(self, record: logging.LogRecord) -> str:
        recordcopy = copy(record)
        separator = " " * (9 - len(recordcopy.levelname))
        recordcopy.__dict__["separator"] = separator
        return super().formatMessage(recordcopy)


if app_config.DEBUG:
    stream_handler = colorlog.StreamHandler()
    custom_formatter = CustomFormatter(
        (
            "%(log_color)s%(levelname)s%(white)s:%(separator)s%(message)s"
            " %(thin)s[%(asctime)s.%(msecs)03d]"
        ),
        log_colors={
            "DEBUG": "blue",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    stream_handler.setFormatter(custom_formatter)
    stream_handler.setLevel(logging.DEBUG)
    logger = colorlog.getLogger("blackfish")
    logger.addHandler(stream_handler)
    logger.setLevel(logging.DEBUG)
else:
    file_handler = logging.FileHandler(f"{os.path.join(app_config.HOME_DIR, 'logs')}")
    formatter = logging.Formatter(
        "[%(asctime)s.%(msecs)03d] %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    logger = colorlog.getLogger("blackfish")
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
