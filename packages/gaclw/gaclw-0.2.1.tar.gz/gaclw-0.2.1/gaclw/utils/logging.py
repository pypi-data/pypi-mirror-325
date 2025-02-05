import logging
import sys

from gaclw.core.config import settings


def get_logger(level: int = settings.LOG_LEVEL) -> logging.Logger:
    """generate logger instance

    Args:
        level (int, optional): logging level. defaults to 2.

    Returns:
        logging.Logger: logger instance
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(level * 10)
    if not logger.hasHandlers():
        # ログを標準出力する
        handler = logging.StreamHandler(stream=sys.stdout)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s",
            datefmt=r"%Y-%m-%dT%H:%M:%S%z",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger


logger = get_logger()
