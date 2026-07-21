
run with:
uv run uvicorn main:app --reload --port 8000

routers/ — the HTTP contract layer. Defines endpoints, request/response shapes. Knows nothing about how work gets done, only what comes in and goes out.

app.routers.generate docs:
https://fastapi.tiangolo.com/tutorial/body/#create-your-data-model
APIRouter: https://fastapi.tiangolo.com/tutorial/bigger-applications/

services/ — the logic layer. Talks to Anthropic, does the actual work. Knows nothing about HTTP.
config.py — settings, loaded from .env once.



Q for claude: ok great, please now explain anthropic_client.py. explain the convention app.config. is def just a function? it sets values for the different variable and what does the -> str do?  client is the anthropic object correct? is .messages is a call from the class where the create function exists, correct? can you point me to the docs for this?  for system that is passed into the function, it wasnt initialize to anything right? or does just pass something that must be a string? and explain the last parameter messages, what is it setting? is this for each potential user i.e. craft impact or burney or whatever? and the last line, is block.text native to python? and does it join to "" if block.type is a string? and explain why i need an anthropic client class. can you explain how join works, the syntax. give me a simple example and then explain this one you did.

For the generate.py,  point me to the relevant docs please. and from app.services.ant... I want the docs too. Is this generate request the main content generation call for our app? will we require different types of routers later on? why do you pass BaseModel for GenerateR* models? what could the user be?

 FastAPI (this file):

Bigger apps / APIRouter (why routers exist, how to split files) → https://fastapi.tiangolo.com/tutorial/bigger-applications/
Request body with Pydantic models → https://fastapi.tiangolo.com/tutorial/body/
response_model → https://fastapi.tiangolo.com/tutorial/response-model/
Path operation decorators (@router.post, etc.) → https://fastapi.tiangolo.com/tutorial/first-steps/
Handling errors (you'll want this soon) → https://fastapi.tiangolo.com/tutorial/handling-errors/
Pydantic (the BaseModel classes):

Models overview → https://docs.pydantic.dev/latest/concepts/models/
Fields & defaults → https://docs.pydantic.dev/latest/concepts/fields/
Anthropic (inside the service generate calls):

Messages API reference → https://docs.anthropic.com/en/api/messages
Python SDK → https://github.com/anthropics/anthropic-sdk-python
Python (import mechanics, str.join):

Modules & packages → https://docs.python.org/3/tutorial/modules.html
str.join → https://docs.python.org/3/library/stdtypes.html#str.join
