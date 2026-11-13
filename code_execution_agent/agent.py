from google.adk.agents import Agent
from google.adk.code_executors import BuiltInCodeExecutor

root_agent = Agent(
    model= 'gemini-3.7-flash',
    name = 'root_agent',
    description= "A helpful agent that can write and run python code.",
    instruction= """Answer the user query accurately. When a question involves calculation, data analysis and anything that benefits from running code, Write Python code and executeand explain it.""",
    code_executor= BuiltInCodeExecutor()
)
