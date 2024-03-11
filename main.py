from fastapi import FastAPI
from src.routers.student import student_router

app = FastAPI()
app.include_router(student_router, prefix="/students", tags=["students"])

@app.get("/")
async def root():
    return {"message": "Welcome to SICEI API"}