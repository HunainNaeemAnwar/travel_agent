from agents import Agent

from instructions import get_explore_instruction
from external_model import MODEL


# Function to create a ExploreAgent with specific instructions
def explore_agent() -> Agent:
    """An agent that suggests places to explore in a country."""
    print("Calling Explore Agent...")
    agent = Agent(
        name="Explore Agent",
        instructions=get_explore_instruction,
        model=MODEL,
    )
    return agent
