from fastapi import FastAPI

app = FastAPI(
    title="Civil AI API",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "status": "running",
        "project": "Civil AI"
    }
