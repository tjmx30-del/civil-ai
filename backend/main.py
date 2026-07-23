from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from openai import OpenAI
import fitz
import os

app = FastAPI()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.get("/")
def home():
    return {"status":"Civil AI Running"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    pdf = fitz.open(
        stream=await file.read(),
        filetype="pdf"
    )

    text = ""

    for page in pdf:
        text += page.get_text()

    prompt = f"""
คุณคือวิศวกรโยธา

วิเคราะห์แบบก่อสร้างต่อไปนี้

{text[:12000]}

ให้ตอบเป็น

1.สรุปแบบ

2.ชนิดงาน

3.รายการวัสดุ

4.รายการที่ควรตรวจสอบ

5.ข้อผิดพลาดที่พบ
"""

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return {
        "analysis": response.choices[0].message.content
    }
