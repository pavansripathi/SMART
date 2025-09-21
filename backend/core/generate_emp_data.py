import sys
import os

# Add backend folder to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# ---------------- Setup ----------------
db_path = "backend/data/smart.db"
if os.path.exists(db_path):
    os.remove(db_path)

import random
import json
import secrets
import numpy as np
from faker import Faker

from backend.db import SessionLocal
from backend.core.employees import Employee

faker = Faker("en_IN")
used_emails = set()
num_of_employees = 1000
total_emp_data = []

# ---------------- Skill Book ----------------
skill_book = [
    "Python", "Java", "JavaScript", "C++", "C#", "SQL", "NoSQL", "HTML", "CSS",
    "TypeScript", "React", "Angular", "Node.js", "Django", "Flask", "Spring Boot",
    "Docker", "Kubernetes", "AWS", "Azure", "GCP", "Linux", "Git",
    "Machine Learning", "Data Analysis"
]

# ---------------- Experience Dataset ----------------
numbers = np.arange(1, 26)  # 1 to 25 years
k = 0.2  # Decay rate (higher = fewer seniors)
probabilities = np.exp(-k * numbers)
probabilities /= probabilities.sum()
np.random.seed(42)
experiences_dataset = np.random.choice(numbers, size=num_of_employees, p=probabilities)

# ---------------- Location Dataset ----------------
locations = ["Amarvathi", "Hyderabad", "Bangalore", "Chennai", "Pune", "Ahmedabad"]
numbers = np.arange(1, len(locations) + 1)
probabilities = np.exp(-k * numbers)
probabilities /= probabilities.sum()
np.random.seed(42)
locations_dataset = np.random.choice(locations, size=num_of_employees, p=probabilities)

# ---------------- Skill Analyzer ----------------
class SkillAnalyzer:
    type_weights = {"low": 0.25, "medium": 0.5, "ok": 0.75, "good": 1, "great": 1.25, "exceptional": 1.5}
    type_to_comp = {
        "low":        [1, 1, 2],
        "medium":     [1, 2, 2, 3],
        "ok":         [2, 2, 3, 3, 4],
        "good":       [3, 3, 4, 4, 5],
        "great":      [4, 5, 5],
        "exceptional":[5, 5, 5]
    }

    def __init__(self, experience: int, emp_type: str):
        self.exp = experience
        self.type = emp_type
        self.weight = self.type_weights[self.type]

    def create_data(self):
        # Skill count grows with experience
        if self.exp <= 1:
            number_of_skills = secrets.choice([1, 2])
        elif self.exp <= 4:
            number_of_skills = secrets.choice([2, 3, 4])
        elif self.exp <= 10:
            number_of_skills = secrets.choice([3, 4, 5])
        else:
            number_of_skills = secrets.choice([4, 5, 6, 7])

        number_of_skills = min(len(skill_book), number_of_skills)

        # Pick random skills
        chosen_skills = random.sample(skill_book, number_of_skills)

        # Assign competency per skill
        skills_with_comp_level = {skill: secrets.choice(self.type_to_comp[self.type]) for skill in chosen_skills}

        # Salary model
        base_salary = 300_000  # entry level
        salary = int(base_salary + self.exp * 100_000 * self.weight)

        return skills_with_comp_level, salary

# ---------------- Helpers ----------------
def generate_email(name: str) -> str:
    base = name.replace(" ", ".").lower()
    email = f"{base}@company.com"
    counter = 1
    while email in used_emails:
        email = f"{base}{counter}@company.com"
        counter += 1
    used_emails.add(email)
    return email

def pick_emp_type(exp: int) -> str:
    if exp <= 2:
        return secrets.choice(["low", "medium", "ok"])
    elif exp <= 5:
        return secrets.choice(["medium", "ok", "good"])
    elif exp <= 10:
        return secrets.choice(["ok", "good", "great"])
    elif exp <= 20:
        return secrets.choice(["good", "great", "exceptional"])
    else:
        return secrets.choice(["great", "exceptional"])

def generate_emp_details(name: str, exp: int, index: int, emp_type: str) -> dict:
    email = generate_email(name)
    location = locations_dataset[index]

    emp_obj = SkillAnalyzer(exp, emp_type)
    skill_profile, salary = emp_obj.create_data()

    return {
        "name": name,
        "email": email,
        "experience": exp,
        "location": location,
        "skills": json.dumps(skill_profile),
        "salary": salary
    }

# ---------------- Seeding ----------------
def seed_employees(num_of_employees: int):
    session = SessionLocal()

    for i in range(num_of_employees):
        exp = int(experiences_dataset[i])
        emp_type = pick_emp_type(exp)
        name = faker.name()
        total_emp_data.append(generate_emp_details(name, exp, i, emp_type))

    employee_objects = [Employee(**emp) for emp in total_emp_data]
    session.add_all(employee_objects)
    session.commit()
    session.close()
    print(f"Inserted {num_of_employees} employee details into the db.")

def print_employees(limit=20):
    session = SessionLocal()
    employees = session.query(Employee).limit(limit).all()
    for emp in employees:
        print(f"ID: {emp.id}")
        print(f"Name: {emp.name}")
        print(f"Email: {emp.email}")
        print(f"Experience: {emp.experience} years")
        print(f"Location: {emp.location}")
        print(f"Salary: {emp.salary}")
        print(f"Skills: {json.loads(emp.skills)}")
        print("-" * 40)
    session.close()

# ---------------- Main ----------------
if __name__ == "__main__":
    seed_employees(num_of_employees)
    print_employees(50)
