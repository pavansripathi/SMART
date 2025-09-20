# Fast API Backend
from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from backend.db import SessionLocal
from backend.core.employees import Employee
from fastapi import Depends

app = FastAPI(title="SMART API")

# dependency to get db connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "SMART API is running"}

@app.get("/employees")
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return employees

@app.get("/employees/{emp_id}")
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == emp_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee
