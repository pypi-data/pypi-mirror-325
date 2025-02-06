# -*- coding: utf-8 -*-
import io
import logging
import os
import sys
import typing
from datetime import datetime
from pathlib import Path

import colorama
from dateutil import tz

from ezpy_logs.delete_old_logs import delete_old_logs
from ezpy_logs.disable_external_loggers import disable_external_loggers

MIN_LEVEL_FOR_LOGGERS = logging.DEBUG
BASE_LOG_DIR = ".logs"

class TqdmToLogger(io.StringIO):
    """Output stream for TQDM which will output to logger module instead of the StdOut."""

    logger = None
    level = None
    buf = ""

    def __init__(self, logger, level=None):
        super().__init__()
        self.logger = logger
        self.level = level or logging.INFO

    def write(self, buf):
        self.buf = buf.strip("\r\n\t ")

    def flush(self):
        self.logger.log(self.level, self.buf)


class ColorFormatter(logging.Formatter):

    formats_color_level: typing.ClassVar = {
        logging.DEBUG: colorama.Fore.GREEN,
        logging.INFO: colorama.Fore.BLUE,
        logging.WARNING: colorama.Fore.YELLOW,
        logging.ERROR: colorama.Fore.MAGENTA,
        logging.CRITICAL: colorama.Fore.RED,
    }

    def format(self, record):
        color = self.formats_color_level.get(record.levelno)

        def get_terminal_format(color):
            return f"{color}%(levelname)-7s : %(relativeCreated)7d ms [Thread %(thread)-5d] %(pathname)50s:%(lineno)-4s ||{colorama.Fore.RESET}  %(message)s"

        log_fmt = get_terminal_format(color)
        formatter = logging.Formatter(
            log_fmt,
            datefmt="%m/%d/%Y %H:%M:%S",
        )
        return formatter.format(record)


class LevelFilter(logging.Filter):
    def __init__(self, low=logging.DEBUG, high=logging.CRITICAL) -> None:
        """Filters by logging level.

        Args:
            low : Lowest passing level (** Included **)
            high : Highest passing level (** Included **)
        """
        self._low = low
        self._high = high
        logging.Filter.__init__(self)

    def filter(self, record):
        if self._low <= record.levelno <= self._high:
            return True
        return False


class LoggerFactory:
    is_setup: typing.ClassVar = False
    output_files: list[tuple[str, int, int, str]] = []  # noqa: RUF012
    min_stdout = logging.DEBUG
    max_stdout = logging.INFO
    min_stderr = logging.WARN
    max_stderr = logging.CRITICAL
    dateformat = "%m/%d/%Y %H:%M:%S"
    terminal_format_str = "%(levelname)-7s : %(relativeCreated)7d ms [Thread %(thread)-5d] %(pathname)50s:%(lineno)-4s ||  %(message)s"
    file_format_str = "%(levelname)s %(asctime)s | [%(relativeCreated)d] Thread %(thread)-5d || [%(pathname)s:%(lineno)s] %(funcName)s || %(message)s"
    # Will hold a list of replaced files to prevent double erasing
    replaced: list[str] = []  # noqa: RUF012
    # List of already setup loggers to prevent duplcate handlers
    setup_loggers: list[str] = []  # noqa: RUF012

    @classmethod
    def add_output_file(
        cls,
        output_file: str,
        min_level=logging.INFO,
        max_level=logging.CRITICAL,
        mode: str = "append",
    ):
        """Adds an additional output file. With a level filter (min and max_level INCLUDED)
        relative paths are relative to working directory.

        Args:
            mode: 'append' or 'replace' (reset will delete the file if it exists)
        """
        cls.output_files.append((output_file, min_level, max_level, mode))

    @classmethod
    def setup_LoggerFactory(cls, log_dir: str = BASE_LOG_DIR, clean_old_logs: bool = True):
        if LoggerFactory.is_setup is True:
            return

        # logging.getLogger() with no argument for name so it's root logger,
        # The interest in this choice is so we can use this root loger settings for all
        # others loggers because of their attribute logger.propagate = True
        # This is recomended from the python logging documentation
        #   See note: https://docs.python.org/3/library/logging.html#logging.Logger.propagate
        root_logger = logging.getLogger()
        LoggerFactory.setup_logger(root_logger)

        log_dir = Path(log_dir).absolute().as_posix()
        _dir_create_archive(cls, log_dir=log_dir)
        is_in_pytest = os.environ.get("PYTEST_CURRENT_TEST", False)
        is_in_ci = os.environ.get("CI", False)
        if is_in_pytest and not is_in_ci:
            _dir_create_latest(cls, log_dir=log_dir)

        # disable_external_loggers("ezpy_logs")

        if clean_old_logs:
            delete_old_logs(log_dir, n_days=30)

        LoggerFactory.is_setup = True
        cls.getLogger(__name__).debug(f"Logging setup complete ! {log_dir = }")
        cls.base_logging_directory = log_dir

    @classmethod
    def setup_logger(cls, logger: logging.Logger):
        """Setup for the logger with the default handlers.

        Will attach handler for stdout, stderr and multiple files.

        Args:
            logger (logging.Logger): usually from  logging.getLogger(__name__)
        """
        log_file_formatter = logging.Formatter(
            cls.file_format_str,
            datefmt=cls.dateformat,
        )
        log_std_formatter = ColorFormatter()
        logging.Formatter(
            cls.terminal_format_str,
            datefmt=cls.dateformat,
        )

        # Setup STDOUT Handler
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(logging.DEBUG)
        stdout_handler.addFilter(LevelFilter(cls.min_stdout, cls.max_stdout))
        stdout_handler.setFormatter(log_std_formatter)
        logger.addHandler(stdout_handler)

        # Setup STDERR Handler
        stderr_handler = logging.StreamHandler(sys.stderr)
        stderr_handler.setLevel(logging.WARNING)
        stderr_handler.addFilter(LevelFilter(cls.min_stderr, cls.max_stderr))
        stderr_handler.setFormatter(log_std_formatter)
        logger.addHandler(stderr_handler)

        # Setup FILEs Handler
        for file_, min_level, max_level, mode in cls.output_files:
            os.makedirs(os.path.dirname(file_), exist_ok=True)
            to_replace = mode == "replace" and file_ not in cls.replaced
            exists = os.path.exists(file_)
            if to_replace and exists:
                os.remove(file_)
                cls.replaced.append(file_)
            file_handler = logging.FileHandler(file_, encoding="utf8")
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(log_file_formatter)
            file_handler.addFilter(LevelFilter(min_level, max_level))
            logger.addHandler(file_handler)
        return logger

    @classmethod
    def getLogger(
        cls,
        name: str = "should be __name__",
        level=MIN_LEVEL_FOR_LOGGERS,
    ) -> logging.Logger:
        cls.setup_LoggerFactory()
        logger = logging.getLogger(name)

        if name in cls.setup_loggers:
            logger.setLevel(level)
            return logger

        logger.propagate = False
        logger = cls.setup_logger(logger)
        logger.setLevel(level)
        cls.setup_loggers.append(name)
        return logger

    @classmethod
    def get_TqdmToLogger(
        cls,
        logger: logging.Logger,
        level=MIN_LEVEL_FOR_LOGGERS,
    ) -> TqdmToLogger:
        # logger = cls.getLogger(name)
        return TqdmToLogger(logger, level)

    @classmethod
    def change_level_of_all_loggers(
        cls,
        level,
    ):
        for name in cls.setup_loggers:
            logger = logging.getLogger(name)
            logger.setLevel(level)


def _dir_create_latest(cls: LoggerFactory, log_dir: str):
    # We add non timestamped Latest and latest_error in replace mode (they will delete the previous files to only contoin this runs logs)
    # Notice the min and max levels for the latest_error file
    cls.add_output_file(
        output_file=os.path.join(
            log_dir,  # circular import otherwise
            # config.settings.directories.app_logging,
            "Latest_ERRORS.log",
        ),
        min_level=logging.WARN,
        max_level=logging.CRITICAL,
        mode="replace",
    )
    cls.add_output_file(
        output_file=os.path.join(
            log_dir,  # circular import otherwise
            # config.settings.directories.app_logging,
            "Latest.log",
        ),
        min_level=logging.DEBUG,
        max_level=logging.CRITICAL,
        mode="replace",
    )


def _dir_create_archive(cls: LoggerFactory, log_dir: str):
    # We add a timestamped log
    time_now = datetime.now(tz=tz.gettz("France/Paris")).strftime("%Y-%m-%d_%H-%M-%S")
    cls.add_output_file(
        output_file=os.path.join(
            log_dir,  # circular import otherwise
            # config.settings.directories.app_logging,
            "archive_ERRORS",
            time_now + ".log",
        ),
        min_level=logging.WARN,
        max_level=logging.CRITICAL,
        mode="append",
    )
    cls.add_output_file(
        output_file=os.path.join(
            log_dir,  # circular import otherwise
            # config.settings.directories.app_logging,
            "archive",
            time_now + ".log",
        ),
        min_level=logging.DEBUG,
        max_level=logging.CRITICAL,
        mode="append",
    )


# * Log from anywhere in the project:
# *
# * 	from src_log.LoggerFactory import LoggerFactory
# *
# *     logger1 = LoggerFactory.getLogger(__name__)
# *

# Or with tqdm:

# * from src_log.LoggerFactory import LoggerFactory
# * from tqdm import tqdm
# * logger1 = LoggerFactory.getLogger(__name__)
# * tqdm_out = LoggerFactory.get_TqdmToLogger(logger1)
# * for name in tqdm(files, file=tqdm_out, miniters=1e4, maxinterval=float("inf")):
# *     ...
