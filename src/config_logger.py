"""Utilities for configuring application logging."""

import logging, logging.config
import os
from pathlib import Path

app_config_dir = os.path.join(os.path.dirname(__file__), "..", "config")


def configure_logging():
    """Configure and return the application logger.

    Returns
    -------
    logging.Logger
        Configured root logger for the application.
    """

    print("Start of logging configuration")
    logging.config.fileConfig(
        Path(app_config_dir, "logging.ini"), disable_existing_loggers=True
    )
    logger = logging.getLogger(__name__)

    logger.info(f"Logger configured was: {logging.getLogger().handlers}")
    return logger
