from fastmcp import FastMCP
import random
import json

mcp = FastMCP("Simple Calculator Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Returns the sum of two numbers.
    
    Args: 
    a: The first number.
    b: The second number.
    
    Returns:
        The sum of a and b.
    """
    return a + b

@mcp.tool
def random_number(min_value: int=1, max_value: int=100) -> int:
    """Generates a random integer between min_value and max_value.
    
    Args:
    min_value (int): The minimum value (default 1).
    max_value (int): The maximum value (default 100).
    
    Returns:
    int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

@mcp.resource("info://server")
def server_info() -> str:
    """Provides information about the calculator server."""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0",
        "description": "A server with basic math tools.",
        "tools": ["add", "random_number"],
        "author": "FastMCP Team"
    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)