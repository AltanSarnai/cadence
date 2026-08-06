from pydantic import BaseModel
from fastapi import APIRouter
from app.services.anthropic_client import generate_response
from app.database import Session
from app.models import Client 

#/api/generate
router = APIRouter(prefix="/api", tags=["generate"])

class GenerateRequest(BaseModel):
    system: str # Should be Craft's rules for content generation. Right now it has a bunch of stuff..
    user: str   # Format/instructions(about format)/Topic/Angle to Use
    model: str = "claude-sonnet-4-6"
    max_tokens: int = 1024

class GenerateResponse(BaseModel):
    text: str

@router.post("/generate", response_model=GenerateResponse)    
def generate(id: int, format: str, request: GenerateRequest):

    augment_user: str

    with Session.begin() as session:
        client = session.query(Client).get(id)
        augment_user = f"""
        Client: {client.name}
        Brand Profile: {client.brand_profile}
        Description: {client.description}
        Key Values: {client.key_values}
        Target Audience:{client.target_audience}

        Request: {request.user}
        """
        #having tone would be good too

    msg = generate_response(
        system=request.system,
        user=augment_user, 
        model=request.model,
        max_tokens=request.max_tokens
        )
    return GenerateResponse(msg=msg)


