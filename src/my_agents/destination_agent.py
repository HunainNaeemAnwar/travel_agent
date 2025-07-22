from agents import Agent

from instructions import get_destination_instruction
from external_model import MODEL


# Function to create a DestinationAgent with specific instructions
def destination_agent() -> Agent:
    """An agent that provides travel-related information for a specific destination."""
    print("Calling Destination Agent...")
    agent = Agent(
        name="Destination Information Agent",
        instructions=get_destination_instruction,
        model=MODEL,
    )
    return agent
