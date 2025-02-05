import logging

logger = logging.getLogger("logger")
logger.setLevel(logging.DEBUG)

if not logger.handlers:
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s(%(lineno)d) - %(message)s")
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


