from .brain import think
from .tools import execute_tool

async def run_agent(user_input: str) -> str:
    messages = [{"role": "user", "content": user_input}]
    
    # الـ Agent loop
    while True:
        response = think(messages)
        
        # لو مفيش tool calls — خلص
        if response.stop_reason == "end_turn":
            for block in response.content:
                if hasattr(block, "text"):
                    return block.text
        
        # لو في tool call — نفذه
        if response.stop_reason == "tool_use":
            # اضيف رد Claude للـ messages
            messages.append({
                "role": "assistant",
                "content": response.content
            })
            
            # نفذ كل tool
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    result = await execute_tool(block.name, block.input)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })
            
            # اضيف النتيجة للـ messages
            messages.append({
                "role": "user",
                "content": tool_results
            })