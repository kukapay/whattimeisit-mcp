from mcp.server.fastmcp import FastMCP
import httpx
import asyncio

# Initialize the MCP server
mcp = FastMCP("WhatTimeIsIt")

# Define a tool to fetch only the current time from World Time API
@mcp.tool()
async def what_time_is_it() -> str:
    """Returns the current time string based on the client's IP using World Time API."""
    url = "https://worldtimeapi.org/api/ip"  # World Time API endpoint for IP-based time
    async with httpx.AsyncClient() as client:
        try:
            # Make an asynchronous GET request to the API
            response = await client.get(url)
            # Raise an exception if the HTTP request fails
            response.raise_for_status()
            # Extract and return only the 'datetime' field from the JSON response
            return response.json()["datetime"]
        except httpx.HTTPStatusError as e:
            # Handle HTTP errors and return an error message
            return f"Error: Failed to fetch time - {str(e)}"
        except Exception as e:
            # Handle unexpected errors and return an error message
            return f"Error: Unexpected issue - {str(e)}"

# Start the server
if __name__ == "__main__":
    mcp.run()
