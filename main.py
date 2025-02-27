from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = []

class Student(BaseModel):
    id: int
    name: str
    age: int

@app.get("/")
def read_root():
    return {"msg": "Hello World"}

@app.get("/students")
def read_students():
    return students

@app.get("/students/{student_id}")
def read_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.post("/students")
def create_student(student: Student):
    for existing_student in students:
        if existing_student.id == student.id:
            raise HTTPException(status_code=400, detail="Student ID already exists")
    students.append(student)
    return student

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"msg": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")