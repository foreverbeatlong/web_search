from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.applications import Starlette
from starlette.routing import Mount
import requests
from bs4 import BeautifulSoup

mcp = FastMCP("My App")

@mcp.tool()
async def web_search(url:str) -> str:
    """返回网页请求的HTML内容'"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.text

app = Starlette(
    routes=[
        Mount('/', app=mcp.sse_app()),
    ]
)
