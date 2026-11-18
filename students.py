from fastapi import APIRouter

# ఇక్కడ FastAPI() కి బదులు APIRouter() వాడుతున్నాం
router = APIRouter()

STUDENTS = [
    {"id": 1, "name": "John Doe", "age": 20},
    {"id": 2, "name": "Jane Smith", "age": 22}
]

# @app బదులు @router వాడుతున్నాం
@router.get("/students")
def get_students():
    return STUDENTS

@router.post("/create_students")
def createStudent():
    return {"message": "Create Student Method - Testing FastAPI"}

@router.put("/update_students")
def updateStudent():
    return {"message": "Update Student Method - Testing FastAPI"}

@router.delete("/delete_students")
def deleteStudent():
    return {"message": "Delete Student Method - Testing FastAPI"}



