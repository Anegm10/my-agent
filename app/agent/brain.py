import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

tools = [
    {
        "name": "search_web",
        "description": "ابحث على الإنترنت عن أي معلومة",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "الموضوع اللي هتبحث عنه"
                }
            },
            "required": ["query"]
        }
    }
]

def think(messages: list) -> dict:
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        tools=tools,
        messages=messages
    )
    return response