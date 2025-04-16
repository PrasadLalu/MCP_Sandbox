import uvicorn
from fastmcp import FastMCP
from fastapi import FastAPI, Body


app = FastAPI()
mcp = FastMCP("MCP Demo Server")


@mcp.tool()
def multiply(a, b):
    return a * b


@app.post("/mcp/multiply")
def call_multiply(data: dict = Body(...)):
    return {"result": multiply(data.get("a", 0), data.get("b", 0))}


@app.get("/")
def home():
    return {"message": "Welcome to MCP server..."}


if __name__ == "__main__":
    uvicorn.run(app)
