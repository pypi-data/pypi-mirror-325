import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_message(message):
    """Helper function for logging messages."""
    logger.info(message)
