import logging
from logging.handlers import RotatingFileHandler
from .api_handler import LoggerHandler
from .config import Config
from .formatter import CustomFormatter


def get_handlers_data():
    config = Config()
    formatter = CustomFormatter()

    service_name = config.get("service_name")
    logging_api_url = config.get('logging_ms_url')
    logging_api_key = config.get('logging_ms_key')

    log_print = config.get('log_print', default=False)
    log_store = config.get('log_store', default=False)
    log_level = getattr(logging, config.get('log_level', default='INFO'))

    handlers = []

    if logging_api_url and logging_api_key and service_name:
        api_handler = LoggerHandler(
            service_name=service_name,
            logging_api_url=logging_api_url,
            logging_api_key=logging_api_key,
        )
        api_handler.setLevel(log_level)
        api_handler.setFormatter(formatter)
        handlers.append(api_handler)

    if log_print:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(formatter)
        handlers.append(console_handler)

    if log_store:
        log_file_name = config.get('log_file_name')
        log_file_backup_count = config.get('log_file_backup_count')
        log_file_max_size = config.get('log_file_max_size')
        rotating_handler = RotatingFileHandler(log_file_name, maxBytes=log_file_max_size, backupCount=log_file_backup_count)
        rotating_handler.setLevel(log_level)
        rotating_handler.setFormatter(formatter)
        handlers.append(rotating_handler)

    return handlers, log_level
