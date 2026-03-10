import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def think(messages: list) -> str:
    last_message = messages[-1]["content"]
    response = model.generate_content(last_message)
    return response.text