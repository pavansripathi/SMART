# SMART Project User Guide (Phase‑0 Deep Dive)

> Comprehensive documentation of Phase‑0 journey — setup, commands, meanings, debugging notes, DevOps insights, and architectural thoughts.

This file lives under `docs/` in the repo.

---

## 📁 Phase‑0 Tickets & Learnings

### ✅ P0‑01 — Monorepo Setup

```
SMART/
 ├─ backend/
 ├─ cli/
 ├─ data/
 └─ docs/
```

### ✅ P0‑02 — FastAPI Skeleton

Run API locally:

```
uvicorn backend.app:app --reload
```

Meaning (detailed):

* `uvicorn` → ASGI server
* `backend.app` → module path (`backend/app.py`)
* `:app` → FastAPI instance inside file
* `--reload` → auto restart on code changes

### ✅ P0‑03 — CLI Bootstrap

```
python cli/main.py
```

Outputs: `SMART CLI ready`

### ✅ P0‑04 — Pytest

```
pytest
```

Ensures testing pipeline works early.

### ✅ P0‑05 — Code Quality

Tools: `black`, `ruff`, `isort`, `pre‑commit`

Commit flow:

```
git add .
git commit -m "msg"
# if auto‑formatted → run commit again
```

### ✅ P0‑06 — Docker Backend

Concepts:

* Images = immutable templates
* Containers = running instances
* Layers = cached build steps
* Volume mount = live reload

### ✅ P0‑07 — GitHub CI

Runs tests + lint on push/PR (like Jenkins)

### ✅ P0‑08 — Raw Data Seed

Added `data/raw/employees.xlsx`

### ✅ P0‑09 — Dev Docs

Moved detailed docs to `/docs`.

---

## 🧰 Installation

```
python -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
pip install pytest black ruff isort pre‑commit
pre‑commit install
```

---

## ▶️ Commands

| Purpose      | Command                                                                                                                            |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| Run API      | `uvicorn backend.app:app --reload`  # Uvicorn (ASGI server) loads module `backend.app`, finds object `app`, reloads on file change |
| Run CLI      | `python cli/main.py`                                                                                                               |
| Tests        | `pytest`  # Discovers tests automatically, runs test functions prefixed with `test_`                                               |
| Lint         | `ruff check .`  # Fast Python linter, checks for style & errors, suggests fixes                                                    |
| Format check | `black --check .`  # Verifies formatting; `black .` auto-formats the entire codebase                                               |
| Imports      | `isort . --check-only`  # Ensures imports are sorted; `isort .` auto-sorts all imports                                             |
| Docker       | `docker compose up --build`  # Builds image if needed, then starts container; `--build` forces rebuild if code changed             |

---

## 🐳 Docker Tips

```
docker compose down --volumes --remove-orphans
docker compose build --no-cache
docker compose up
```

---

## 🔧 Git Lessons

* `git reflog` recovers lost commits
* `--force-with-lease` safer than `--force`
* Pre‑commit ≠ CI → local vs remote guardrails

---

## 🧠 Engineering Principles

* Walking skeleton first
* Automate quality
* Fail fast
* Document learning
* Think architecture, build small

---

## 🚀 Future Direction

* `.env` config loader
* PostgreSQL + SQLAlchemy / SQLModel
* Vector DB for skills search
* Containerized microservices
* CI → security + build + tests

---

## End of Phase‑0

Core structure ready. Phase‑1 → Data ingestion & transformation.

This document contains detailed installation, setup, and development workflows for the SMART project.

> This guide captures every technical step, tool usage, and learning during the project journey.

## 📦 Contents

* Introduction
* Project Architecture
* Setup & Installation
* Running Backend (FastAPI)
* Running CLI
* Linting & Formatting
* Testing
* Pre‑commit Hooks
* Docker Setup & Usage
* CI/CD
* Data Folder & Seed Files
* Troubleshooting
* Notes & Learnings

---

## ✅ Introduction

(This section will describe project motivation, goals, and evolving roadmap.)

---

## 🧠 Project Architecture

(To be filled: Monorepo structure, modules, services overview)

---

## ⚙️ Setup & Installation

(To be filled: virtualenv, dependencies, commands)

---

## ▶️ Running Instructions

(To be filled)

---

## 🧹 Code Quality Tooling

(To be filled: ruff, black, isort details)

---

## 🧪 Testing

(To be filled)

---

## 🐳 Docker

(To be filled)

---

## 🚀 CI/CD

(To be filled)

---

## 📂 Data Folder

(To be filled)

---

## 💡 Notes & Learnings

(To be filled: insights learned as project evolves)

# SMART Project User Guide (Phase‑1 Deep Dive)

# 📘 Database Fundamentals & ORM Concepts — SMART Project Reference

> This document summarizes all the key concepts related to PostgreSQL, SQLAlchemy, ORM, ER diagrams, constraints, indexes, Pydantic schemas, and relationships. Purpose: To ensure clear understanding before implementing Phase 1 (Database Schema Design) of the SMART project.

## 🧠 1️⃣ PostgreSQL Overview
**PostgreSQL** (or **Postgres**) is a powerful **Relational Database Management System (RDBMS)** used for storing and managing structured data.

### ✅ Key Features
- Open-source, highly stable, and enterprise-grade.
- Supports **SQL** (structured) + **JSON/JSONB** (semi-structured) → hybrid RDBMS.
- Provides **ACID compliance** (safe transactions).
- Supports **constraints**, **indexes**, **triggers**, and **foreign keys**.
- Used widely in production systems, analytics, and ML backends.

### Example Data Types
| Type | Example |
|-------|----------|
| INTEGER | 1 |
| VARCHAR(100) | 'Babai' |
| DATE | '2025-11-12' |
| BOOLEAN | TRUE |
| JSONB | {'skill': 'Python', 'level': 'Advanced'} |

## ⚙️ 2️⃣ SQLAlchemy Overview
**SQLAlchemy** is a Python library that provides tools to interact with databases like PostgreSQL. It offers two main layers:  
1. **Core** – Low-level, close to SQL syntax.  
2. **ORM (Object Relational Mapper)** – High-level, uses Python classes to represent tables.

### Why Use SQLAlchemy?
- Manages **database connections** safely.
- Handles **transactions** automatically.
- Prevents **SQL injection** via parameterized queries.
- Lets you switch databases (Postgres, SQLite, MySQL) without code rewrite.
- Integrates perfectly with **FastAPI** and **Pydantic**.

## 🧩 3️⃣ ORM (Object Relational Mapper)
An ORM maps **database tables → Python classes**.

### Example
```python
class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    department = Column(String)
```

### Advantages
- Work with Python objects instead of writing SQL manually.
- Schema and relationships are defined in one place.
- Automatically handles CRUD operations.

### Disadvantages
- Hides actual SQL — slower to learn SQL deeply.
- Slight overhead in complex queries.

## 🧱 4️⃣ Using Raw SQL Inside SQLAlchemy
You can use **pure SQL queries** safely inside SQLAlchemy for learning and control.

### Example
```python
from sqlalchemy import create_engine, text
engine = create_engine("postgresql+psycopg2://postgres:password@localhost:5432/smart")
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE IF NOT EXISTS employees (id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, department VARCHAR(50), joining_date DATE);"))
    conn.execute(text("INSERT INTO employees (name, department) VALUES (:n, :d)"), {"n": "Babai", "d": "AI/ML"})
    result = conn.execute(text("SELECT * FROM employees WHERE department=:d"), {"d": "AI/ML"})
    for row in result:
        print(row.id, row.name)
```

✅ You still get:
- Connection pooling  
- Transaction handling  
- SQL injection protection  

❌ But not:
- ORM features like model mapping, relationship loading, or automatic updates.

## 🔗 5️⃣ Relationships in Databases
Relationships define how tables are connected.

| Type | Meaning | Example |
|------|----------|----------|
| One-to-One | One record linked to one | Employee → ID card |
| One-to-Many | One record linked to many | Department → Employees |
| Many-to-Many | Many linked to many | Employees ↔ Skills |

### Many-to-Many Example
We use a **junction table**:

| Table | Columns |
|--------|----------|
| employees | id, name |
| skills | id, name |
| employee_skills | employee_id (FK), skill_id (FK) |

## 🗺️ 6️⃣ ER Diagram (Entity Relationship Diagram)
A visual representation of entities (tables) and their relationships.

```
Employees ───< Employee_Skills >─── Skills
```

Legend:  
- Each box = table  
- Each line = relationship  
- `<` or `>` shows direction (many-to-one or one-to-many)

## 🧬 7️⃣ Pydantic Schemas
**Pydantic** validates and structures data using Python type hints. Used mainly in **FastAPI** for request/response validation.

### Example
```python
from pydantic import BaseModel
class EmployeeSchema(BaseModel):
    id: int
    name: str
    department: str
```

### Benefits:
- Validates incoming/outgoing API data.
- Enforces type safety.
- Auto-generates OpenAPI docs (in FastAPI).

## 🧩 8️⃣ Constraints & Indexes
### Constraints
Rules that ensure data integrity.

| Constraint | Description | Example |
|-------------|--------------|----------|
| **PRIMARY KEY** | Unique identifier | employee_id |
| **FOREIGN KEY** | Reference to another table | employee_id in employee_skills |
| **UNIQUE** | Prevents duplicates | skill name |
| **NOT NULL** | Value required | employee name |
| **CHECK** | Enforces conditions | salary > 0 |

### Indexes
Speed up lookups by creating quick access paths.  
Use indexes for:
- Foreign keys  
- Frequently searched columns  
- Columns with UNIQUE constraints

## ⚡ 9️⃣ SQLAlchemy ORM vs Raw SQL Comparison
| Feature | ORM | Raw SQL (inside SQLAlchemy) |
|----------|-----|-----------------------------|
| Connection management | ✅ | ✅ |
| Transaction handling | ✅ | ✅ |
| SQL Injection Safety | ✅ | ✅ |
| Object mapping | ✅ | ⚠️ Optional |
| Lazy loading / relationships | ✅ | ❌ |
| Full SQL control | ⚠️ Limited | ✅ |
| Easier debugging | ❌ | ✅ |
| Interview relevance | ⚠️ Medium | ✅ High |

**Conclusion:**  
For SMART Phase 1, raw SQL inside SQLAlchemy is preferred for learning SQL deeply and ensuring clarity.

## 🧭 10️⃣ Professional Recommendation
- Use **SQLAlchemy Engine + raw SQL** for schema creation, CRUD operations, learning SQL syntax, and data extraction for ML models.  
- Introduce **ORM** later (Phase 2) when integrating with FastAPI for cleaner API models.  
- Use **Pydantic schemas** for validation and serialization when moving to REST API development.

## 🧩 11️⃣ Example Query Patterns
### Create Table
```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(50),
    joining_date DATE
);
```
### Insert Data
```sql
INSERT INTO employees (name, department, joining_date)
VALUES ('Babai', 'AI/ML', '2025-11-12');
```
### Select Data
```sql
SELECT id, name FROM employees WHERE department = 'AI/ML';
```
### Join Example
```sql
SELECT e.name, s.name AS skill
FROM employees e
JOIN employee_skills es ON e.id = es.employee_id
JOIN skills s ON s.id = es.skill_id;
```

## 🧩 12️⃣ Hybrid Query Example (Python + SQLAlchemy Engine)
```python
from sqlalchemy import text
from database import engine
with engine.connect() as conn:
    query = text("""SELECT e.name, s.name as skill FROM employees e JOIN employee_skills es ON e.id = es.employee_id JOIN skills s ON s.id = es.skill_id;""")
    result = conn.execute(query)
    for row in result:
        print(row.name, "-", row.skill)
```

## 🧠 Summary
- **PostgreSQL** → actual database engine.  
- **SQLAlchemy** → connection manager / ORM bridge.  
- **ORM** → Pythonic way to work with tables (optional).  
- **Raw SQL** → better for learning and interviews.  
- **Pydantic** → data validation layer for APIs.  
- **Constraints & Indexes** → data safety and performance.  
- **ER Diagram** → visual schema planning.  
- **Many-to-Many relationships** → use junction tables.  

📘 **Next Step:**  
Proceed to design the `P1-01` HR schema using **raw SQL** inside SQLAlchemy — covering: employees, skills, employee_skills with proper **constraints**, **indexes**, and **foreign keys**.

