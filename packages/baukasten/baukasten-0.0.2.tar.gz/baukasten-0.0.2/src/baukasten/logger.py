import logging


def get_logger(name: str = None) -> logging.Logger:
    if name:
        return logging.getLogger(f"{__package__}.{name}")
    else:
        return logging.getLogger(f"{__package__}")


def configure_logging(level: int = logging.INFO):
    logger = logging.getLogger(__package__)
    logger.propagate = False  # Prevent duplicate logs in user's configuration

    # Clear existing handlers
    if logger.handlers:
        for handler in logger.handlers:
            handler.close()
        logger.handlers.clear()

    # Apply configuration
    logger.setLevel(level)
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)