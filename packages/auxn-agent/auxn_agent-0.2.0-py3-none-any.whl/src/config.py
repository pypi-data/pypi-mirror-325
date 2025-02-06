from pathlib import Path
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    # Base paths
    BASE_DIR: Path = Path(__file__).parent.parent
    DATA_DIR: Path = BASE_DIR / "data"
    IMAGE_DIR: Path = DATA_DIR / "images"

    # Playwright settings
    PLAYWRIGHT_TIMEOUT: int = 30000  # milliseconds
    MAX_RETRIES: int = 3
    RETRY_DELAY: int = 1000  # milliseconds
    # Additional Playwright settings
    PAGE_LOAD_TIMEOUT: int = 10000  # milliseconds
    PAGE_LOAD_STATE: str = "networkidle"

    # Database settings
    DB_ECHO: bool = False

    # Initialize directories
    def create_directories(self):
        self.DATA_DIR.mkdir(exist_ok=True)
        self.IMAGE_DIR.mkdir(exist_ok=True)

    # Initialize database
    def setup_database(self):
        """Initialize database after directories are created"""
        self.create_directories()
        # Defer database initialization to avoid circular imports
        from .database.database import db

        db.create_tables()


# Initialize settings first
settings = Settings()
settings.create_directories()  # Create directories first
# Database setup will be handled by the database module
