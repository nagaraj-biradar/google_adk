from pathlib import Path
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

folder = Path(__file__).parent.joinpath("files").resolve()
folder.mkdir(exist_ok=True)

root_agent = Agent(
    name= "filesystem_agent",
    model= 'gemini-3.5-flash-lite',
    instruction= f"Help users manage files in {folder} . Use absolute path.",
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="npx",
                    args = ["-y", "@modelcontextprotocal/server-fliesystem", str(folder)]
                )
            )
        )
    ]
)