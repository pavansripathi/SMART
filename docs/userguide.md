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
