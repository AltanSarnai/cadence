from fastapi import FastAPI
from app.routers import generate, monitor
from fastapi.responses import FileResponse
from pathlib import Path


app = FastAPI(title="Cadence")

app.include_router(generate.router)
app.include_router(monitor.router)

path = Path(__file__).resolve().parent.parent.joinpath('static/index.html')


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/", response_class=FileResponse)
def getHTML():
    return path



'''
@app.post("/generate")
def generate:
    post_body = {}
'''

def main():
    print("Hello from cadence!")


if __name__ == "__main__":
    main()
