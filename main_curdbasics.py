"""
FastAPI application for basic CRUD operations without DB

"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()




@app.get("/")
def index():
    return { "This is Index Method "}




STUDENTS = [
    {"id": 1, "name": "John Doe", "age": 20, "major": "Computer Science"},
    {"id": 2, "name": "Jane Smith", "age": 22, "major": "Mathematics"},
    {"id": 3, "name": "Bob Johnson", "age": 25, "major": "Physics"},
    {"id": 4, "name": "Alice Brown", "age": 21, "major": "Chemistry"},

]
@app.get("/students")
def getAllStudents():
    return STUDENTS



@app.get("/single-student/{student_id}")
def getSingleStudentDetails(student_id: int):
    # 1. లూప్ అందరు స్టూడెంట్స్ ని ఒకరి తర్వాత ఒకరిని చెక్ చేస్తుంది
    for student in STUDENTS:
        if student["id"] == student_id:
            return student  # ఐడీ దొరకగానే ఆ స్టూడెంట్ డేటాని రిటర్న్ చేసి ఫంక్షన్ ఆపేస్తుంది
            
    # 2. లూప్ మొత్తం తిరిగినా ఏ స్టూడెంట్ ఐడీ మ్యాచ్ అవ్వకపోతేనే ఇది రన్ అవుతుంది (లూప్ బయట ఉంది)
    return {"message": "Student not found."}

class StudentSchema(BaseModel):
    name: str
    age: int
    major: str

@app.post("/addNewStudent")
def addNewStudent(student_data: StudentSchema):
    new_id = STUDENTS[-1]["id"] + 1 if STUDENTS else 1

    new_student = {
        "id": new_id,
        "name": student_data.name,
        "age": student_data.age, 
        "major": student_data.major
    }
    STUDENTS.append(new_student)

    return {"message": "New student added successfully.", "student": new_student}


@app.delete("/delete-student/{student_id}")
def deleteStudent(student_id: int):
    for student in STUDENTS:
        if student["id"] == student_id:
            STUDENTS.remove(student)
            return{"message": f"ID {student_id}" " student deleted successfully."}

    return {"message": "Student not found."}




    # Update Student Details  ({"id": 5, "name": "Lakshmi", "age": 21, "major": "Computers"})

@app.get("/update-student/{student_id}")
def update(student_id: int):

    for student in STUDENTS:
        if student["id"] == student_id:
            student["name"] = "Lakshmi"
            student["age"] = 21
            student["major"] = "Computers"
            

    return "This is Update Method"