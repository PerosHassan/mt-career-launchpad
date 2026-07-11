from fastapi import FastAPI
from pydantic import BaseModel
from ai_engine import generate_response

# ============================================================
# MT CAREER LAUNCHPAD API
# ============================================================

app = FastAPI(
    title="MT Career Launchpad API",
    description="Backend API for the MT Career Launchpad AI Assistant",
    version="2.0"
)

# ============================================================
# REQUEST MODEL
# ============================================================

class AIRequest(BaseModel):
    task: str
    input: str

# ============================================================
# HOME ROUTE
# ============================================================

@app.get("/")
def home():
    return {
        "message": "Welcome to the MT Career Launchpad API!",
        "status": "running",
        "version": "2.0"
    }

# ============================================================
# AI GENERATION ROUTE
# ============================================================

@app.post("/generate")
def generate(request: AIRequest):

    response = generate_response(
        task=request.task,
        user_input=request.input
    )

    return {
        "success": True,
        "task": request.task,
        "response": response
    }
