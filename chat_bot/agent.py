from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

groq_llm = LiteLlm(model="groq/openai/gpt-oss-safeguard-20b")
# groq_llm = LiteLlm(model="groq/qwen/qwen3.8-27b")

root_agent = Agent(
    model=groq_llm,
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
