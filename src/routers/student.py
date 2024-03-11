from typing import Dict
from fastapi import APIRouter, HTTPException
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
    return JSONResponse(content=students[student_id], status_code=200)

@student_router.post("/")
def create_student(student: Student):
    if student.id in students:
        return HTTPException(status_code=400, detail="Student already registered")
    students[student.id] = student
    return JSONResponse(content=student, status_code=201)

@student_router.put("/{student_id}")
def update_student(student_id: int, student: StudentUpdate):
    if student_id not in students:
        return HTTPException(status_code=404, detail="Student not found")
    students[student_id] = student
    return JSONResponse(content=student, status_code=200)

@student_router.delete("/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return HTTPException(status_code=404, detail="Student not found")
    students.pop(student_id)
    return JSONResponse(content={"message": "Student deleted successfully"}, status_code=200)