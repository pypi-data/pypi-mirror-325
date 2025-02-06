from typing import Optional, List
from sqlalchemy.orm import Session
from .models import DBListing, DBListingImage  # Fix import path
from ..models.listing import Listing, ListingImage


class ListingCRUD:
    @staticmethod
    def _convert_listing_to_db(listing: Listing) -> dict:
        """Convert Pydantic model to database dictionary"""
        return {
            "id": listing.id,
            "title": listing.title,
            "url": str(listing.url),  # Convert HttpUrl to string
            "price": listing.price,
            "description": listing.description,
        }

    @staticmethod
    def _convert_image_to_db(image: ListingImage) -> dict:
        """Convert image model to database dictionary"""
        return {
            "url": str(image.url),  # Convert HttpUrl to string
            "local_path": image.local_path,
            "screenshot_path": image.screenshot_path,
        }

    @staticmethod
    def create_listing(db: Session, listing: Listing) -> DBListing:
        try:
            db_listing = DBListing(**ListingCRUD._convert_listing_to_db(listing))
            for image in listing.images:
                db_image = DBListingImage(**ListingCRUD._convert_image_to_db(image))
                db_listing.images.append(db_image)
            db.add(db_listing)
            db.flush()  # Ensure the database operation is executed
            db.refresh(db_listing)
            return db_listing
        except Exception as e:
            db.rollback()
            raise e

    @staticmethod
    def get_listing(db: Session, listing_id: str) -> Optional[DBListing]:
        return db.query(DBListing).filter(DBListing.id == listing_id).first()

    @staticmethod
    def get_listings(db: Session, skip: int = 0, limit: int = 100) -> List[DBListing]:
        return db.query(DBListing).offset(skip).limit(limit).all()

    @staticmethod
    def update_listing(
        db: Session, listing_id: str, listing: Listing
    ) -> Optional[DBListing]:
        try:
            db_listing = ListingCRUD.get_listing(db, listing_id)
            if db_listing:
                # Update main fields
                update_data = ListingCRUD._convert_listing_to_db(listing)
                for key, value in update_data.items():
                    setattr(db_listing, key, value)

                # Update images
                db_listing.images.clear()
                for image in listing.images:
                    db_image = DBListingImage(**ListingCRUD._convert_image_to_db(image))
                    db_listing.images.append(db_image)

                db.flush()
            return db_listing
        except Exception as e:
            db.rollback()
            raise e

    @staticmethod
    def delete_listing(db: Session, listing_id: str) -> bool:
        db_listing = ListingCRUD.get_listing(db, listing_id)
        if db_listing:
            db.delete(db_listing)
            return True
        return False
