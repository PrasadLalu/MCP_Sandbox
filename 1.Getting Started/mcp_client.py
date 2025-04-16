import requests


def multiply(a, b):
    url = "http://127.0.0.1:8000/mcp/multiply"
    response = requests.post(url=url, json={"a": a, "b": b})
    if response.status_code == 200:
        print("MCP multiplication called successfully.", response.json()["result"])
    else:
        print("Something went wrong.")
    return None


if __name__ == "__main__":
    multiply(15, 4)
