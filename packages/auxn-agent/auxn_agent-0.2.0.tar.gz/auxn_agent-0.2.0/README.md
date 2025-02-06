# Auxn Agent

## Overview

Auxn Agent is a web scraping and data extraction tool designed to automate the process of collecting information from websites. Built with modern Python async capabilities, it uses Playwright for browser automation and SQLite for efficient data storage.

## Status: Alpha (v0.1.0)

Current test coverage: 84%

### Key Features
- ✅ Asynchronous web scraping with Playwright
- ✅ Automatic pagination handling
- ✅ SQLite database with SQLAlchemy ORM
- ✅ Comprehensive test suite
- ✅ Configurable logging system
- ✅ Type-safe data models with Pydantic

### Requirements
- Python 3.10 or higher
- Poetry for dependency management
- System dependencies for Playwright
  ```bash
  # Ubuntu/Debian
  sudo apt-get install -y \
      libevent-2.1-7 \
      libavif16
  ```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/auxn-agent.git
   cd auxn-agent
   ```

2. Install Poetry (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Install dependencies:
   ```bash
   poetry install
   ```

4. Install Playwright browsers:
   ```bash
   poetry run playwright install chromium
   ```

5. Install browser dependencies:
   ```bash
   poetry run playwright install-deps
   ```

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run with coverage report
poetry run pytest --cov=src

# Run specific test file
poetry run pytest tests/test_scraper.py
```

### Usage Example

```python
from src.scraper.scraper_manager import ScraperManager
import asyncio

async def main():
    manager = ScraperManager()
    listings = await manager.scrape_listings(
        url="https://example.com",
        listing_selector=".listing",
        next_button_selector=".next-page"
    )
    print(f"Found {len(listings)} listings")

if __name__ == "__main__":
    asyncio.run(main())
```

### Project Structure
```
auxn-agent/
├── src/
│   ├── database/        # Database models and CRUD operations
│   ├── models/          # Pydantic data models
│   ├── scraper/         # Web scraping logic
│   └── utils/           # Utilities and helpers
├── tests/              # Test suite
└── poetry.lock        # Dependency lock file
```

### Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Run tests (`poetry run pytest`)
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### License

[MIT](LICENSE)
