from typing import Union

from agents import function_tool

from mock_data import hotels
from models.Hotel import Hotel


@function_tool()
def get_all_hotels(country: str, city: str) -> Union[list[Hotel], str]:
    """
    Retrieves validated hotel listings for a given city and country using a Pydantic model.
    """

    print("Calling get_all_hotels tool...")

    # Step 1: Validate existence of country
    country_data = hotels.get(country)
    if not country_data:
        return f"No hotel data available for {country}."

    # Step 2: Filter city-wise hotels
    matched_hotels = []
    for hotel in country_data:
        hotel_city = hotel.get("city", "").lower()
        if hotel_city == city.lower():
            try:
                matched_hotels.append(Hotel(**hotel))
            except Exception as e:
                print(f"Invalid hotel data skipped: {hotel} | Error: {e}")
    print(f"Found {len(matched_hotels)} hotels in {city}, {country}.")

    # Step 3: Handle no match
    if not matched_hotels:
        return f"No hotels found in {city}, {country}."
    print(f"Found {len(matched_hotels)} hotels in {city}, {country}.")

    return matched_hotels
