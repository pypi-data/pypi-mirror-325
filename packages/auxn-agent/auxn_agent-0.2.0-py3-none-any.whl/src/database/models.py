from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()


class DBListing(Base):
    __tablename__ = "listings"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    price = Column(Float)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    images = relationship("DBListingImage", back_populates="listing")


class DBListingImage(Base):
    __tablename__ = "listing_images"

    id = Column(Integer, primary_key=True)
    listing_id = Column(String, ForeignKey("listings.id"))
    url = Column(String, nullable=False)
    local_path = Column(String)
    screenshot_path = Column(String)

    listing = relationship("DBListing", back_populates="images")
