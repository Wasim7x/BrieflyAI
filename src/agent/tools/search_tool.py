from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode

def get_tools():
    """Returns a list of tools to be used in the agent."""
    tools = [TavilySearch(max_results=2)]
    return tools

def create_tool_nodes(tools):
    """Creates and returns tool nodes for the agent."""
    return ToolNode(tools=tools)