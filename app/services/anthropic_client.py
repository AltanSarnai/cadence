from anthropic import Anthropic
from config import settings

client = Anthropic(
        api_key=settings.api_key #took out anthropic_ because 
                                 #in config it is just api_key too
)

def generate(system: str, user: str, 
             model: str = "claude-sonnet-4-6", 
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
        ]#falta una coma aqui?
    )
    return "".join(block.text for block in message.content 
        if block.type == "text")
