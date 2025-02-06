from loguru import logger
import sys
from pathlib import Path


def setup_logger():
    """Setup logger with error handling"""
    logger.remove()

    # Add console logger with custom format and error handling
    format_str = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
        "<level>{message}</level>"
    )
    logger.add(
        sys.stderr,
        format=format_str,
        level="INFO",
        enqueue=True,
        catch=True,
    )

    # Add file logger with better error handling
    log_path = Path("logs")
    log_path.mkdir(exist_ok=True)

    logger.add(
        str(log_path / "debug.log"),
        rotation="500 MB",
        retention="10 days",
        level="DEBUG",
        enqueue=True,
        catch=True,
        delay=True,
    )


setup_logger()
