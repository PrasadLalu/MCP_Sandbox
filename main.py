# from fastapi import FastAPI
# import uvicorn
# from fastapi_mcp import add_mcp_server

# app = FastAPI()


# @app.get("/")
# def home():
#     return {"message": "Hello FastAPI"}


# if __name__ == "__main__":
#     uvicorn.run(app=app)
    
# add_mcp_server(app, mount_path="/mcp", name="FastMCP")

from fastapi import FastAPI
import uvicorn
from fastapi_mcp import FastMCP, add_mcp_server

app = FastAPI()

# Initialize FastMCP
mcp = FastMCP(name="FastMCP Server")

# Example of an MCP tool (you can add more tools as needed)
@mcp.tool()
def multiply(a: int, b: int):
    return a * b

# Add MCP server to FastAPI app
add_mcp_server(app, mount_path="/mcp", name="FastMCP")

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

