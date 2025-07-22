from pydantic import BaseModel
from typing import Union

from agents import function_tool

from mock_data import flights
from models.Flight import Flight


@function_tool()
def get_all_flights(
    current_country: str,
    current_city: str,
    destination_country: str,
    destination_city: str,
) -> list[Flight] | str:
    """
    Fetches available flight options between two cities and countries.

    Typically used by BookingAgent to simulate flight search results.

    Args:
        current_country (str): Country of departure.
        current_city (str): City of departure.
        destination_country (str): Country of arrival.
        destination_city (str): City of arrival.

    Returns:
        list[Flight] or str: List of validated flight models or an error message.
    """
    print("Calling get_all_flights tool...")

    available_flights = []
    for flight in flights:
        if (
            flight["current_country"].lower() == current_country.lower()
            and flight["current_city"].lower() == current_city.lower()
            and flight["country"].lower() == destination_country.lower()
            and flight["destination"].lower() == destination_city.lower()
        ):
            try:
                available_flights.append(Flight(**flight))
            except Exception as e:
                print(f"Skipped invalid flight: {flight} | Error: {e}")

    if not available_flights:
        return "No flights found for the specified route."

    return available_flights
