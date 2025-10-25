import logging
import logging.config
import os

# ------------------------------
# 1. Set up directories and paths
# ------------------------------

# Get the absolute path to the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create a "logs" folder inside the project if it doesn't exist
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Define the path for the main log file
LOG_FILE = os.path.join(LOG_DIR, "app.log")

# ------------------------------
# 2. Define logging configuration
# ------------------------------

# Logging configuration dictionary using Python's dictConfig format
LOGGING_CONFIG = {
    "version": 1,  # Must be 1 for dictConfig
    "disable_existing_loggers": False,  # Keep existing loggers active
    "formatters": {
        # Simple formatter for console output
        "standard": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
        # Detailed formatter for log files (includes file, line, function)
        "detailed": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - "
                      "%(filename)s:%(lineno)d - %(funcName)s() - %(message)s"
        },
    },
    "handlers": {
        # Console handler: prints logs to terminal
        "console": {
            "class": "logging.StreamHandler",  # Logs to stdout
            "level": "DEBUG",  # Show DEBUG and higher level messages
            "formatter": "standard",  # Use the simple formatter
        },
        # File handler: writes logs to a file with rotation
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",  # Only INFO and higher messages are saved in file
            "formatter": "detailed",  # Detailed info for debugging later
            "filename": LOG_FILE,  # Path to log file
            "maxBytes": 5 * 1024 * 1024,  # Max file size 5 MB
            "backupCount": 5,  # Keep last 5 log files
            "encoding": "utf-8",  # Ensure correct text encoding
        },
    },
    "loggers": {
        # Root logger: used when no specific logger name is requested
        "": {
            "handlers": ["console", "file"],  # Both console and file
            "level": "DEBUG",  # Capture all DEBUG+ messages
            "propagate": False,  # Avoid passing messages to ancestor loggers
        },
        # Example of a module-specific logger
        "my_module": {
            "handlers": ["console", "file"],
            "level": "INFO",  # Capture INFO+ messages for this module
            "propagate": False
        }
    }
}

# ------------------------------
# 3. Apply configuration
# ------------------------------

# Apply the logging configuration using dictConfig
logging.config.dictConfig(LOGGING_CONFIG)

# Create a logger instance to use in your scripts
logger = logging.getLogger(__name__)
