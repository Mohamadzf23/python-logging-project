import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)

file_handler = RotatingFileHandler(
    "app.log",
    maxBytes= 1024 * 1024,
    backupCount= 3
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)