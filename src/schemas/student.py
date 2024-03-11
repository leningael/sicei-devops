from pydantic import BaseModel


class Student(BaseModel):
    id: int
    name: str
    enrollment: str
    
class StudentUpdate(BaseModel):
    name: str
    enrollment: str