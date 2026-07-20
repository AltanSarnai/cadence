from pydantic import BaseModel
from fastapi import APIRouter

from services.anthropic_client import generate

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
    
    msg = generate(**request.model_dump())#model dump for now..
    return GenerateResponse(msg=msg)


