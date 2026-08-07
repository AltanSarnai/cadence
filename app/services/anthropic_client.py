from anthropic import Anthropic
from app.config import settings
from fastapi import HTTPException

client = Anthropic(
        api_key=settings.anthropic_api_key 
)

class InternalError(Exception):
    pass

# TODO add try-catch block.
def generate_response(system: str, user: str, 
             model: str = "claude-sonnet-4-6", 
             max_tokens: int = 100) -> str:
    try:
        print("\n\n\n\nCalling Anthropic... riiing riiiing.\n")
        message = client.messages.create(
            max_tokens=max_tokens,
            system=system,
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": user
                }
            ]#falta una coma aqui?
        )
    except InternalError:
        print("Error talking to Anthropic!")
  
    return "".join(block.text for block in message.content 
        if block.type == "text")


def monitor() -> str:
    return "monitor something"