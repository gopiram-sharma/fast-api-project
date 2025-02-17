import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get log level from environment variable
log_level = os.getenv("LOG_LEVEL", "INFO").upper()
log_location = os.getenv("LOG_LOC")

def get_logger(name: str) -> logging.Logger:
    # Create a custom logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Create handlers
    file_handler = logging.FileHandler(log_location)
    console_handler = logging.StreamHandler()

    # Set level for handlers
    file_handler.setLevel(log_level)
    console_handler.setLevel(log_level)

    # Create formatters and add them to handlers
    formatter = logging.Formatter('%(asctime)s,%(msecs)03d %(name)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger