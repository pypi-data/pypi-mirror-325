import os
import logging
from dotenv import load_dotenv
from colorama import Fore, Style, init

# Load environment variables
load_dotenv()

# Initialize colorama for colored logs in terminal
init(autoreset=True)

# Determine environment
is_production = os.getenv("ENVIRONMENT") != "development"
debug_logging = os.getenv("DEBUG_LOGGING", "0") == "1"

# Logger key
logger_key = os.getenv("LOGGER_KEY", "ot-notifications-server")
logger = logging.getLogger(logger_key)

# Suppress noisy logs from dependencies
noisy_loggers = [
    "uvicorn",
    "uvicorn.error",
    "uvicorn.access",
    "watchfiles",
    "botocore",
    "botocore.tokens",
]
for noisy_logger in noisy_loggers:
    logging.getLogger(noisy_logger).setLevel(logging.WARNING)


class ColoredFormatter(logging.Formatter):
    """Custom log formatter that adds colors to log levels and timestamps."""

    level_colors = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.RED + Style.BRIGHT,
    }
    asctime_color = Fore.CYAN  # Cyan color for timestamp

    def format(self, record):
        """Formats log records with color-coded levels and timestamps."""
        record.asctime = self.formatTime(record, self.datefmt)
        colored_asctime = f"{self.asctime_color}{record.asctime}{Style.RESET_ALL}"
        level_color = self.level_colors.get(record.levelno, "")
        colored_levelname = f"{level_color}{record.levelname}{Style.RESET_ALL}"
        self._style._fmt = self._fmt.replace("%(asctime)s", colored_asctime).replace(
            "%(levelname)s", colored_levelname
        )
        return super().format(record)


# Configure logging format
log_format = (
    "%(asctime)s: %(levelname)s - %(message)s"
    if not is_production
    else "%(name)s | %(asctime)s: %(levelname)s - %(message)s"
)

# Configure logging
log_level = logging.DEBUG if debug_logging else logging.INFO
formatter = ColoredFormatter(fmt=log_format, datefmt="%Y-%m-%d %H:%M:%S")

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.setLevel(log_level)
logger.addHandler(stream_handler)
