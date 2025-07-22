from pydantic import BaseModel

class Hotel(BaseModel):
    name: str
    rating: float
    city: str
    price_per_night: float

    class Config:
        extra = "allow"  # Allow additional fields from mock_data
