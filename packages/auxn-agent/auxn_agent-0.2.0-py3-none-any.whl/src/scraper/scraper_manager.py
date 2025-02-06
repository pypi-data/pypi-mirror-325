from typing import List, Optional
from loguru import logger
from pydantic import ValidationError
from .playwright_scraper import PlaywrightScraper
from ..models.listing import Listing, ListingImage
from ..config import settings
from ..database import db, ListingCRUD
from sqlalchemy.orm import Session


class ScraperManager:
    def __init__(self):
        scraper_timeout = 30000
        scraper_retry_delay = 1000
        self.scraper = PlaywrightScraper(
            timeout=scraper_timeout, retry_delay=scraper_retry_delay
        )

    async def scrape_listings(
        self,
        url: str,
        listing_selector: str,
        next_button_selector: str,
        *,  # Force keyword arguments after this point
        test_db: Optional[Session] = None,
    ) -> List[Listing]:
        """Scrape all listings from multiple pages"""
        listings = []
        try:
            await self.scraper.start()
            try:
                first_page = True
                while True:
                    # Navigate only on the first page; let pagination handle subsequent pages
                    if first_page:
                        if not await self.scraper.navigate(url):
                            break
                        first_page = False

                    # Extract listings from current page
                    page_listings = await self.scraper.extract_listings(
                        listing_selector
                    )

                    # Process and store listings
                    for listing_data in page_listings:
                        listing = await self._process_listing(listing_data, test_db)
                        if listing:
                            listings.append(listing)

                    # Handle pagination
                    if not await self.scraper.handle_pagination(next_button_selector):
                        break
            finally:
                await self.scraper.close()

        except Exception as e:
            error_msg = f"Error in scrape_listings: {str(e)}"
            logger.error(error_msg)
        return listings

    async def _process_listing(
        self,
        listing_data: dict,
        test_db: Optional[Session] = None,
    ) -> Optional[Listing]:
        """Process and validate listing data"""
        try:
            if not all(key in listing_data for key in ["title", "url"]):
                logger.warning(
                    f"Missing required fields in listing data: {listing_data}"
                )
                return None

            # Provide default values for missing fields
            if "id" not in listing_data:
                import uuid

                listing_data["id"] = str(uuid.uuid4())
            if "description" not in listing_data:
                listing_data["description"] = ""

            listing_id = listing_data.get("id")
            screenshot_path = settings.IMAGE_DIR / f"{listing_id}.png"

            if not await self.scraper.take_screenshot(str(screenshot_path)):
                logger.error("Failed to capture screenshot")
                return None
            try:
                listing = Listing(
                    **listing_data,
                    images=[
                        ListingImage(
                            url=listing_data["url"],
                            screenshot_path=str(screenshot_path),
                        )
                    ],
                )
            except ValidationError as e:
                logger.error(f"Validation error creating listing: {e}")
                return None

            # Store in database
            try:
                if test_db:
                    ListingCRUD.create_listing(test_db, listing)
                else:
                    with db.get_session() as session:
                        ListingCRUD.create_listing(session, listing)
            except Exception as e:
                logger.error(f"Database error storing listing: {e}")
                return None

            return listing

        except Exception as e:
            logger.error(f"Error processing listing: {str(e)}")
            return None
