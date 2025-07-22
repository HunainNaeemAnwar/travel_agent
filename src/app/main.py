from typing import cast

from agents import Agent, Runner, handoff
import chainlit as cl


from instructions import get_orchestrator_instruction
from external_model import MODEL
from my_agents import explore_agent, destination_agent, booking_agent
from tools import get_native_language


def orchestrator_agent() -> Agent:
    """
    This function creates an orchestrator agent that manages the workflow of other agents.
    It can be used to coordinate tasks, manage dependencies, and ensure that the overall
    process runs smoothly.
    """
    # Create an instance of the Agent class for the orchestrator

    agent = Agent(
        name="orchestrator_agent",
        instructions=get_orchestrator_instruction(),
        handoffs=[
            handoff(explore_agent()),
            handoff(destination_agent()),
            handoff(booking_agent()),
        ],
        tools=[get_native_language],
        model=MODEL,
    )

    return agent


@cl.on_chat_start
async def start():
    agent = orchestrator_agent()
    cl.user_session.set("chat_history", [])
    cl.user_session.set("agent", agent)
    await cl.Message(content="Hello wanna book flight").send()


@cl.on_message
async def main(message: cl.Message):
    history = cl.user_session.get("chat_history") or []
    history.append({"role": "user", "content": message.content})

    msg: cl.Message = cl.Message(content="")
    await msg.send()

    agent: Agent = cast(Agent, cl.user_session.get("agent"))
    try:
        result = await Runner.run(agent, history)
        msg.content = result.final_output
        await msg.update()
        history.append({"role": "assistant", "content": msg.content})
        cl.user_session.set("chat_history", history)
        print(f"User: {message.content}")
        print(f"Assistant: {msg.content}")

    except Exception as e:
        print(f"Error: {e}")
        msg.content = f"Error: {e}"
        await msg.update()
