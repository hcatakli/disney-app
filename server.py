from mcp.server.fastmcp import FastMCP
from app import getDisneyCharacter

# Initialize MCP server
mcp = FastMCP("disney-mcp")

@mcp.tool()
def get_character_info(medicine_name: str) -> str:
    """
    get information about a Disney character by name.
    """
    character_info = getDisneyCharacter(medicine_name)
    return character_info

if __name__ == "__main__":
    mcp.run(transport="stdio")