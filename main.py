from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from pydantic import BaseModel
from dotenv import load_dotenv
import logging
import os
import time

from chat_response import get_answer
from email_notifier import send_email

# Load environment variables from .env
load_dotenv()

app = FastAPI()

# Add X-Frame-Options and CORS headers for iframe usage
@app.middleware("http")
async def add_headers(request, call_next):
    response: Response = await call_next(request)
    response.headers["X-Frame-Options"] = "ALLOWALL"
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

# Add CORS support for external embedding
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Enable logging to file
logging.basicConfig(filename="chatbot.log", level=logging.INFO)

# Serve static files (e.g. script.js)
app.mount("/static", StaticFiles(directory="static"), name="static")

# In-memory rate limiter
request_times = {}

class RateLimiterMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if request.url.path == "/chat" and request.method == "POST":
            ip = request.client.host
            now = time.time()
            if ip in request_times and now - request_times[ip] < 1:
                return JSONResponse({"detail": "Rate limit exceeded"}, status_code=429)
            request_times[ip] = now
        return await call_next(request)

app.add_middleware(RateLimiterMiddleware)

# Route for full chatbot demo (can be used internally)
@app.get("/", response_class=HTMLResponse)
async def root():
    with open("templates/plugin.html") as f:
        return HTMLResponse(content=f.read())

# Route for iframe plugin version
@app.get("/plugin", response_class=HTMLResponse)
async def plugin_embed():
    with open("templates/plugin.html") as f:
        return HTMLResponse(content=f.read())

# Chat request model
class ChatRequest(BaseModel):
    message: str

# Chat handler API
@app.post("/chat")
async def chat(request_data: ChatRequest):
    message = request_data.message
    response = get_answer(message)
    logging.info(f"User: {message} | Bot: {response}")
    if not response:
        send_email("Unanswered question", f"User asked: {message}")
        response = "I'm not sure about that. A team member will get back to you."
    return {"reply": response}
