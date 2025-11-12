from fastmcp import FastMCP

mcp = FastMCP.as_proxy(
    "https://bottom-moccasin-opossum.fastmcp.app/mcp",
    name = "My Server Proxy"
)

if __name__ == "__main__":
    mcp.run()