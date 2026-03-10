import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def think(messages: list) -> str:
    last_message = messages[-1]["content"]
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=last_message
    )
    return response.text