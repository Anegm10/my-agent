from .brain import think

async def run_agent(user_input: str) -> str:
    messages = [{"role": "user", "content": user_input}]
    response = think(messages)
    return response