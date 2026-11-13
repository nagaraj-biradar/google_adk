from google.adk.agents import Agent
from dotenv import load_dotenv

load_dotenv()

root_agent = Agent(
    name= 'root_agent',
    description= '',
    model= 'gemini-3.6-flash',
    instruction= ''
)