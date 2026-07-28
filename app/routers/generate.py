from pydantic import BaseModel
from fastapi import APIRouter
from app.services.anthropic_client import generate_response

#/api/generate
router = APIRouter(prefix="/api", tags=["generate"])

class GenerateRequest(BaseModel):
    system: str
    user: str
    model: str = "claude-sonnet-4-6"
    max_tokens: int = 1024

class GenerateResponse(BaseModel):
    text: str

@router.post("/generate", response_model=GenerateResponse)    
def generate(request: GenerateRequest):
    
    msg = generate_response(
        system=request.system,
        user=request.user, 
        model=request.model,
        max_tokens=request.max_tokens
        )
    return GenerateResponse(msg=msg)


