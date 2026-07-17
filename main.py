from fastapi import FastAPI

app = FastAPI(title="Cadence")

@app.get("/health")

def health():
    return {"status": "ok"}

def main():
    print("Hello from cadence!")


if __name__ == "__main__":
    main()
