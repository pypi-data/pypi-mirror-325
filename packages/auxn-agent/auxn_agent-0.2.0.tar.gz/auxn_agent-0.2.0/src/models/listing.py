from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional, List


class ListingImage(BaseModel):
    url: HttpUrl
    local_path: Optional[str] = None
    screenshot_path: Optional[str] = None


class Listing(BaseModel):
    id: str
    title: str
    url: HttpUrl
    price: Optional[float]
    description: Optional[str]
    images: List[ListingImage] = []
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
