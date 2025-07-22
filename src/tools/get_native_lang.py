from agents import Agent, function_tool, Runner

from external_model import MODEL


@function_tool
async def get_native_language(text: str, location: str) -> str:
    """
    Translates the final message from the Orchestrator Agent into the target language.

    This tool should only be used by the Orchestrator Agent, and only once the final message
    (to be delivered to the user) has been constructed in English or the system’s default language.

    Parameters:
        text (str): The full message the orchestrator intends to send to the user.
        language (str): The name of the target language for translation (e.g., "French", "Japanese", "Urdu").

    Returns:
        str: The translated version of the input message, in the specified target language.

    Notes:
        - Do NOT use this tool inside other specialized agents like DestinationAgent, BookingAgent, or ExploreAgent.
        - The translation should reflect the natural tone and formality of the target language.
        - If the language is unsupported or translation fails, the original message should be returned unchanged.
    """
    print("Calling get_native_language tool...")
    agent = Agent(
        name="translation_agent",
        instructions=f"Translate the given text into the {location} language.",
        model=MODEL,
    )
    result = await Runner.run(agent, input=text)
    translated_text = result.final_output

    return translated_text
