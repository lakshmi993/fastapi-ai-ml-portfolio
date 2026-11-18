from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import students  # students.py ఫైల్‌ని ఇంపోర్ట్ చేస్తున్నాం

app = FastAPI()

# స్టాటిక్ ఫైల్స్ కనెక్షన్
app.mount("/static", StaticFiles(directory="staticfiles"), name="static")

# students.py లోని రూట్స్ అన్నీ ఇక్కడికి లింక్ చేస్తున్నాం
app.include_router(students.router)

@app.get("/") 
def index():
    return {"message": "Index Method - Testing FastAPI"}
