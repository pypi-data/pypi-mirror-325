# -*- coding: utf-8 -*-
import logging

DEFAULT_LOGGER_NAMES = [
    # "sqlalchemy",
]

def disable_external_loggers(internal_logger, logger_names: list[str] | None = None):
    """Disable most external loggers.

    Turning logging on makes the console very noisy. Use this function to disable most
    loggers except ours.
    """
    if logger_names is None:
        logger_names = DEFAULT_LOGGER_NAMES
    for logger_name in logger_names:
        logging.getLogger(logger_name).disabled = True

    for v in logging.Logger.manager.loggerDict.values():
        if type(v) is not logging.Logger:
            continue
        try:
            if (
                not v.name.startswith(internal_logger)
            ):
                v.disabled = True
        except Exception:
            pass
