
from google.adk.agents import Agent

root_agent = Agent(
    name="root_agent",
    model='gemini-3.6-flash',
    description="You are a helpfull assistant for user questions.",
    instruction="Answer user query to the best of your knowledge",
)
