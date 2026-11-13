from google.adk.agents.llm_agent import Agent
from google.adk.tools.google_search_tool import google_search
from dotenv import load_dotenv

load_dotenv()

# groq_llm = LiteLlm(model="groq/openai/gpt-oss-safeguard-20b")
# groq_llm = LiteLlm(model="groq/qwen/qwen3.8-27b")

root_agent = Agent(
    model='gemini-3.7-flash',
    name='root_agent',
    description='A helpful assistant that can search web.',
    instruction='Answer user questions accurately. Use Google Search tool when you need current information or need to verify the facts.',
    tools=[google_search]
)
