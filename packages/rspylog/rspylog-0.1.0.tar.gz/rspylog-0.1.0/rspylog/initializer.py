import logging
from .config import Config
from .handlers import get_handlers_data


def configure_dt_logging():
    config = Config()
    celery_mode = config.get('celery_mode', False)

    handlers, log_level = get_handlers_data()
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    celery_logger = logging.getLogger('celery')

    if celery_mode:
        celery_logger.setLevel(log_level)

    for handle in handlers:
        root_logger.addHandler(handle)
        if celery_mode:
            celery_logger.addHandler(handle)


def celery_logger_handler(logger, propagate):
    config = Config()
    celery_mode = config.get('celery_mode', False)
    if celery_mode:
        handlers, log_level = get_handlers_data()
        logger.logLevel = log_level
        logger.propagate = propagate
        for handle in handlers:
            logger.addHandler(handle)
    else:
        return None

