import os
from fastapi import FastAPI
from pydantic import BaseModel
from app.agent.graph import run_agent

app = FastAPI(title="My AI Agent")

class AgentRequest(BaseModel):
    input: str

@app.get("/")
def home():
    return {"status": "Agent is running! 🚀"}

@app.post("/agent/run")
async def run(request: AgentRequest):
    result = await run_agent(request.input)
    return {"response": result}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)