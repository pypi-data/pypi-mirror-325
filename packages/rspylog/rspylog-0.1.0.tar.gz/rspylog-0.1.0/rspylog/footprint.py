import logging


def leave(
        log_type: str,
        message: str | None = None,
        **kwargs,
):
    logger = logging.getLogger()

    data = dict(
        msg=message,
        extra={
            'details': kwargs,
        }
    )

    if log_type.lower() == "warning":
        logger.warning(**data)
    elif log_type.lower() == "error":
        logger.error(**data)
    elif log_type.lower() == "warning":
        logger.warning(**data)
    elif log_type.lower() == "debug":
        logger.debug(**data)
    else:
        logger.info(**data)
