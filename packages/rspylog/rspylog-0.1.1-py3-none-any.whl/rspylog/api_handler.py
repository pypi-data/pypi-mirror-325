import json
import logging
import requests
from time import sleep


class Logger:
    def __init__(self, logging_api_url, logging_api_key):
        self.api_url = logging_api_url
        self.api_key = logging_api_key

        self.headers = {
            "Authorization": f"{self.api_key}",
            "Content-Type": "application/json"
        }

    def log(self, details: dict):
        max_retries = 5
        backoff_seconds = 3
        for attempt in range(1, max_retries + 1):
            try:
                response = requests.post(
                    url=self.api_url,
                    json=json.loads(json.dumps(details, default=str)),
                    headers=self.headers
                )
                response.raise_for_status()
                return True
            except requests.exceptions.RequestException as e:
                if attempt < max_retries:
                    sleep(backoff_seconds)
                else:
                    logging.error(f"Failed to send log to API: {e}")
                    raise


class LoggerHandler(logging.Handler):
    def __init__(self, logging_api_url, logging_api_key):
        super().__init__()
        self.logger = Logger(
            logging_api_url=logging_api_url,
            logging_api_key=logging_api_key,
        )

    def emit(self, record):
        details = record.__dict__.get('details')
        if details is not None:
            self.logger.log(details=details)
