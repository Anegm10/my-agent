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