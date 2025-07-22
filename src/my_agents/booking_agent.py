from agents import Agent
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX

from instructions import get_booking_agent_instructions
from external_model import MODEL
from tools import get_all_flights, get_all_hotels


# Function to create a BookingAgent with specific instructions
def booking_agent() -> Agent:
    """An agent that handles flight and hotel bookings."""
    print("Calling Booking Agent...")
    agent = Agent(
        name="Booking Agent",
        instructions=f"""{RECOMMENDED_PROMPT_PREFIX} {get_booking_agent_instructions}""",
        model=MODEL,
        tools=[get_all_flights, get_all_hotels],
    )
    return agent
