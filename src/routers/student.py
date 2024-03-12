from typing import Dict
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.schemas.student import Student, StudentUpdate

students: Dict[int, Student] = {}

student_router = APIRouter()

@student_router.get("/")
def get_students():
    return list(students.values())

@student_router.get("/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        return HTTPException(status_code=404, detail="Student not found")
    return students[student_id]

@student_router.post("/")
def create_student(student: Student):
    if student.id in students:
        return HTTPException(status_code=400, detail="Student already registered")
    students[student.id] = student
    return JSONResponse(content=jsonable_encoder(student), status_code=201)

@student_router.put("/{student_id}")
def update_student(student_id: int, student: StudentUpdate):
    if student_id not in students:
        return HTTPException(status_code=404, detail="Student not found")
    updated_student = Student(id=student_id, **student.model_dump())
    students[student_id] = updated_student
    return updated_student

@student_router.delete("/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return HTTPException(status_code=404, detail="Student not found")
    students.pop(student_id)
    return {"message": "Student deleted successfully"}