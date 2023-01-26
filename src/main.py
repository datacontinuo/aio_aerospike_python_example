from fastapi import FastAPI

from routers import (
    students,
    teachers,
    schools,
    parents
)


app = FastAPI()


app.include_router(students.router, prefix="/api/v1/students", tags=["students"])
app.include_router(teachers.router, prefix="/api/v1/teachers", tags=["teachers"])
app.include_router(schools.router, prefix="/api/v1/schools", tags=["schools"])
app.include_router(parents.router, prefix="/api/v1/parents", tags=["parents"])
