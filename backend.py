from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
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
# CORS CONFIGURATION
# ============================================================

# This ensures your Streamlit frontend can securely request data 
# from this API when hosted on Render.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
# HEALTH CHECK ROUTE
# ============================================================

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "MT Career Launchpad Backend"
    }

# ============================================================
# AI GENERATION ROUTE
# ============================================================

@app.post("/generate")
def generate(request: AIRequest):
    try:
        response = generate_response(
            task=request.task,
            user_input=request.input
        )
        
        return {
            "success": True,
            "task": request.task,
            "response": response
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"An error occurred in the backend: {str(e)}"
        )
