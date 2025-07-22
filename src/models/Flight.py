from pydantic import BaseModel


class Flight(BaseModel):
    current_country: str
    current_city: str
    country: str
    destination: str
    date: str
    flight_number: str
    airline: str
    duration: str
    price: float
