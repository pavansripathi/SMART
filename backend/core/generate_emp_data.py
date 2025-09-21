import sys
import os
import numpy as np

db_path = "backend/data/smart.db"
if os.path.exists(db_path):
    os.remove(db_path)

# Add backend folder to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
print(sys.path)

from faker import Faker
import random
import json
from backend.db import SessionLocal
from backend.core.employees import Employee

faker = Faker('en_IN')
used_emails = set()
num_of_employees = 1000
total_emp_data = []
count = 0

numbers = np.arange(1, 25)
k = 0.2 # Decay rate, adjust higher for steeper decay
probabilities = np.exp(-k*numbers)
probabilities /= probabilities.sum() # Normalize

# Generate dataset of 100 numbers (seed for reproducibility)
np.random.seed(42)
experiences_dataset = np.random.choice(numbers, size=1000, p=probabilities)

def generate_email(name):
    # We need to generate unique emails
    count = 0
    base = name.replace(" ", ".")
    email = base + "@company.com"
    while email in used_emails:
        count += 1
        email = base + str(count) + "@company.com"
    used_emails.add(email)
    
    return email

def generate_skills(num):
    # generate skills and competency levels based on input numbers
    skills_and_levels = {}
    total_skills = ["python", "CI/CD", "java", "JS", "ML", "AI"]
    for skill in random.sample(total_skills, num):
        skills_and_levels[skill] = random.randint(1,5)
    
    return skills_and_levels
        
def generate_emp_details(name, experience=0):
    # generate all the employees details like name, email, skills and competency levels
    emp_details = {}
    email = generate_email(name)
    skills_and_levels = generate_skills(random.randint(3, 6))
    location = random.choice(["Amarvathi", "Hyderabad", "Bangalore", "Pune", "Ahmedabad"])
    
    return {"name":name, "email":email, "experience":experience, "location":location, "skills":json.dumps(skills_and_levels)} 

def seed_employees(num_of_employees):
    # seed employees data into the data base
    session = SessionLocal()
    
    for i in range(num_of_employees):
        name = faker.name()
        total_emp_data.append(generate_emp_details(name, int(experiences_dataset[i])))
    
    employee_objects = [Employee(**emp) for emp in total_emp_data]
    session.add_all(employee_objects)
    session.commit()
    session.close()
    print(f"Inserted {num_of_employees} employee details into the db.")

def print_employees(limit=100):
    # Used for developing and debugging
    session = SessionLocal()
    employees = session.query(Employee).limit(limit).all()
    for emp in employees:
        print(f"ID: {emp.id}")
        print(f"Name: {emp.name}")
        print(f"Email: {emp.email}")
        print(f"Experience in years: {emp.experience}")
        print(f"Location: {emp.location}")
        print(f"Skills: {json.loads(emp.skills)}")  # convert JSON string back to dict
        print("-" * 40)
    session.close()

if __name__ == "__main__":
    seed_employees(num_of_employees)
    print_employees(10)
