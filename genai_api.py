from fastapi import FastAPI
from pydantic import BaseModel, Field
from google import genai

# 1. Initialize FastAPI application

app = FastAPI(
    title="GenAI Chatbot API",
    description="FastAPI backed connected to Google Gemini LLM",
    version="1.0.0"
)

# 2. Initialize Gemini Client (Paste your API key inside quotes)
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
client = genai.Client(api_key=GEMINI_API_KEY)

# 3. Define Input Schema using Pydantic

class ChatPrompt(BaseModel):
    question: str = Field(..., min_length=2, description="Ask any question to the AI")

@app.get("/")
def home():
    return {"status": "Online", "message": "GenAI Chatbot API is ready!"}

# 4. GenAI Chat Endpoint

@app.post("/ask-ai")
def ask_gemini(prompt: ChatPrompt):
    # Send the user's question to Gemini 2.5 Flash model
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt.question

    )

    return {
        "question": prompt.question,
        "ai_answer": response.text
    }