from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI(title="Civil AI")

@app.get("/")
def root():
    return {
        "status": "ok",
        "app": "Civil AI",
        "version": "1.0"
    }

@app.get("/health")
def health():
    return {
        "health": "good"
    }

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    return JSONResponse({
        "filename": file.filename,
        "message": "PDF uploaded successfully",
        "result": "AI analysis will be available in the next step."
    })
