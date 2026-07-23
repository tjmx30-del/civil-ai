from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import fitz

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Civil AI Running"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    pdf = fitz.open(stream=await file.read(), filetype="pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    return JSONResponse({
        "success": True,
        "pages": len(pdf),
        "text": text[:5000]
    })
