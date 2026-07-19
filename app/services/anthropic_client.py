from anthropic import Anthropic
from app.config import settings

client = Anthropic(
        api_key=settings.anthropic_api_key
)

def generate(system: str, user: str, model: str = "claude-sonnet-4-6", 
             max_tokens: int = 1024) -> str:
    message = client.messages.create(
        max_tokens=max_tokens,
        system=system,
        model=model,
        messages=[
            {
                "role": "user",
                "content": user

            }
        ]#falta una coma?
    )
    