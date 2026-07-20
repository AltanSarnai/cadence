from fastapi import FastAPI

from routers import generate

app = FastAPI(title="Cadence")

app.include_router(generate.router)

@app.get("/health")

def health():
    return {"status": "ok"}

'''
@app.post("/generate")
def generate:
    post_body = {}
'''
def main():
    print("Hello from cadence!")


if __name__ == "__main__":
    main()
