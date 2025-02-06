from playwright.async_api import async_playwright, Browser
from loguru import logger
from typing import Optional, List, Dict
import asyncio
from ..config import settings


class PlaywrightScraper:
    def __init__(self, timeout: int = None, retry_delay: int = None):
        from ..config import settings

        self.timeout = timeout if timeout is not None else settings.PLAYWRIGHT_TIMEOUT
        self.retry_delay = (
            retry_delay if retry_delay is not None else settings.RETRY_DELAY
        )
        self.browser: Optional[Browser] = None
        self.context = None
        self.page = None
        self._playwright = None

    async def __aenter__(self):
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def start(self):
        """Initialize the browser and create new context"""
        self._playwright = await async_playwright().start()
        self.browser = await self._playwright.chromium.launch(headless=True)
        self.context = await self.browser.new_context(ignore_https_errors=True)
        self.page = await self.context.new_page()

    async def close(self):
        """Close all browser instances and cleanup"""
        try:
            if self.page:
                try:
                    await self.page.close()
                except Exception as e:
                    logger.error(f"Error closing page: {e}")
            if self.context:
                try:
                    await self.context.close()  # Removed timeout parameter
                except Exception as e:
                    logger.error(f"Error closing context: {e}")
            if self.browser:
                try:
                    await self.browser.close()
                except Exception as e:
                    logger.error(f"Error closing browser: {e}")
            if self._playwright:
                try:
                    await self._playwright.stop()
                except Exception as e:
                    logger.error(f"Error stopping playwright: {e}")
        except Exception as e:
            logger.error(f"Error during cleanup: {str(e)}")
        finally:
            self.page = None
            self.context = None
            self.browser = None
            self._playwright = None

    async def navigate(self, url: str, retries: int = None) -> bool:
        from ..config import settings

        retries = retries if retries is not None else settings.MAX_RETRIES
        for attempt in range(retries):
            try:
                await self.page.goto(url, timeout=self.timeout)
                return True
            except Exception as e:
                logger.warning(
                    f"Navigation failed (attempt {attempt + 1}/{retries}): {str(e)}"
                )
                if attempt < retries - 1:
                    await asyncio.sleep(self.retry_delay / 1000)
                else:
                    logger.error(
                        f"Failed to navigate to {url} after {retries} attempts"
                    )
                    return False

    async def take_screenshot(self, path: str) -> bool:
        """Take a full page screenshot"""
        try:
            await self.page.screenshot(path=path, full_page=True)
            return True
        except Exception as e:
            # Handle target closure errors gracefully
            if "TargetClosedError" in str(e):
                logger.error("Target page closed during screenshot capture.")
            else:
                logger.error(f"Screenshot failed: {str(e)}")
            return False

    async def extract_listings(self, selector: str) -> List[Dict]:
        """Extract listing data from current page"""
        listings = []
        try:
            elements = await self.page.query_selector_all(selector)
            for element in elements:
                listing_data = {}
                # Extract title
                title_elem = await element.query_selector("h2")
                if title_elem:
                    listing_data["title"] = await title_elem.inner_text()

                # Extract URL
                url_elem = await element.query_selector("a")
                if url_elem:
                    listing_data["url"] = await url_elem.get_attribute("href")

                # Extract price
                price_elem = await element.query_selector(".price")
                if price_elem:
                    price_text = await price_elem.inner_text()
                    listing_data["price"] = self._parse_price(price_text)

                listings.append(listing_data)
        except Exception as e:
            logger.error(f"Error extracting listings: {str(e)}")

        return listings

    async def handle_pagination(self, next_button_selector: str) -> bool:
        """Handle pagination by clicking next button if available"""
        try:
            next_button = await self.page.query_selector(next_button_selector)
            if next_button and await next_button.is_visible():
                # Wait for button to be ready
                await next_button.wait_for_element_state("stable")

                # Click with wait options
                async with self.page.expect_navigation(
                    wait_until=settings.PAGE_LOAD_STATE,
                    timeout=settings.PAGE_LOAD_TIMEOUT,
                ):
                    await next_button.click()

                # Additional safety check
                await self.page.wait_for_load_state(
                    state=settings.PAGE_LOAD_STATE, timeout=settings.PAGE_LOAD_TIMEOUT
                )
                return True
            return False
        except Exception as e:
            logger.error(f"Pagination error: {str(e)}")
            return False

    def _parse_price(self, price_text: str) -> Optional[float]:
        """Parse price text to float"""
        try:
            # Remove currency symbols and convert to float
            clean_price = "".join(filter(lambda x: x.isdigit() or x == ".", price_text))
            return float(clean_price)
        except ValueError:
            return None
