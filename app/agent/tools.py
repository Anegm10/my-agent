import httpx

async def search_web(query: str) -> str:
    url = f"https://api.duckduckgo.com/?q={query}&format=json&no_html=1"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        result = data.get("AbstractText", "")
        if not result:
            result = f"نتيجة البحث عن: {query} — جرب تسأل بطريقة تانية"
        return result

async def execute_tool(tool_name: str, tool_input: dict) -> str:
    if tool_name == "search_web":
        return await search_web(tool_input["query"])
    return "Tool مش موجود"