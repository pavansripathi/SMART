# 📌 SMART Project — Phased CI/CD Build Plan (Vertical Slice Approach)

This document outlines a **phased development roadmap** for the SMART Talent Intelligence system, following real-world engineering practices:

✅ Iterative & incremental delivery  
✅ Vertical slice development  
✅ Walking skeleton → feature expansion  
✅ CI/CD & quality gates at every step  

---

## 🧠 What This Approach Is Technically Called
- **Vertical Slice Architecture**
- **Walking Skeleton Development**
- **Iterative & Incremental Delivery**s
- **Agile CI/CD Workflow**
- **Trunk‑Based Development**

---

## 🏁 Phase 0 — Project Bootstrap (Walking Skeleton)

### 🎯 Goal
Repo + tools + empty working services + CI pipeline

### ✅ Tasks
- Create monorepo structure (`backend/`, `cli/`, `ui/`, `data/`)
- `pyproject.toml` + `pre‑commit`
- Minimal FastAPI + health check (`/`)
- Basic CLI placeholder
- Add unit test framework (`pytest`)
- Linting: black + ruff + isort
- Dockerfile + docker-compose
- GitHub CI: lint + test

### 🎁 Deliverable
- Code runs locally + CI green  
- `GET /` returns 200

---

## 📊 Phase 1 — Schema, Seed Data, API Contracts

### 🎯 Goal
DB + schema + initial seed data + GET endpoints

### ✅ Tasks
- DB schema (employees, skills, employee_skills)
- Seed CSV + loader script
- Alembic migrations
- FastAPI endpoints:
  - `GET /employees`
  - `GET /employees/{id}`
- Write OpenAPI contract
- Add 6–10 unit tests

### 🎁 Deliverable
- Database + read-only API + test suite

---

## 💻 Phase 2 — CLI MVP (Employer Matching, Rule‑Based)

### 🎯 Goal
CLI tool to rank employees by skill/experience/etc.

### ✅ Tasks
- CLI command: `smart-match`
- Inputs:
  ```
  --skills
  --min-exp
  --location
  --availability
  --top-k
  ```
- Rule‑based scoring v1:
  ```
  score = 0.6*skill_overlap + 0.25*experience + 0.10*location + 0.05*availability
  ```
- Pretty‑table output + CSV export
- Unit tests

### 🎁 Deliverable
- `smart-match --skills "python,sql" --top-k 5`
- Table of sorted candidates

---

## 🌐 Phase 3 — Match API (Rule-Based)

### 🎯 Goal
Expose matching via FastAPI

### ✅ Tasks
- `POST /match`
- Input JSON → score response
- Reuse CLI logic
- Streamlit demo UI page
- Integration tests

### 🎁 Deliverable
- API + basic UI view for matching

---

## 📝 Phase 4 — Resume Skill Extraction (Baseline NLP)

### 🎯 Goal
Extract skills from text resumes (keyword‑based baseline)

### ✅ Tasks
- Define skill dictionary
- NLP script + tests
- `POST /resume/extract`
- Batch update DB from resumes

### 🎁 Deliverable
- Resume → list of skills

---

## 🤖 Phase 5 — Embeddings + Vector Search

### 🎯 Goal
Semantic talent matching

### ✅ Tasks
- Load sentence‑transformer (MiniLM)
- Embeddings for:
  - employees
  - job queries
- FAISS/Qdrant vector DB
- New mode: `semantic` + `hybrid` scoring

### 🎁 Deliverable
- `/match?mode=semantic|hybrid`

---

## ⚙️ Phase 6 — Evaluator + Configurable Scoring

### 🎯 Goal
Testable ranking improvements

### ✅ Tasks
- Store weights in YAML
- Offline evaluation:
  - `MAP@k`, `NDCG@k`
- MLflow tracking

### 🎁 Deliverable
- Evaluation script + metrics logged

---

## 🔐 Phase 7 — Auth + RBAC + Audit Logs

### 🎯 Goal
Enterprise basic security

### ✅ Tasks
- JWT login
- Roles: Admin / HR / Manager
- Protect `/match`, `/employees`
- Audit log DB table

### 🎁 Deliverable
- Secure matching API

---

## 🖥️ Phase 8 — Streamlit UI (HR Console)

### 🎯 Goal
Basic UI for matching & browsing employees

### ✅ Tasks
- Employee list page
- Match page (form inputs)
- Results table & CSV export

### 🎁 Deliverable
- Usable HR web app

---

## 💬 Phase 9 — Resume RAG Chat

### 🎯 Goal
Chat with a resume / candidate profile

### ✅ Tasks
- Embed resume chunks
- Retrieval + prompt chain
- `POST /resume/chat`
- Streamlit chat UI

### 🎁 Deliverable
- AI answers about candidate resume

---

## 📈 Phase 10 — Monitoring & Drift Alerts

### 🎯 Goal
Add observability

### ✅ Tasks
- Prometheus metrics
- Grafana dashboards
- EvidentlyAI drift check

### 🎁 Deliverable
- System & ML monitoring live

---

## 🚀 Phase 11 — CICD + Docker Release Pipeline

### 🎯 Goal
Automated build + test + deploy

### ✅ Tasks
- Multi‑stage Docker build
- GitHub Actions deploy pipeline
- Version tags

### 🎁 Deliverable
- Push to main triggers build + push image

---

## 👤 Phase 12 — Employee Portal (MVP)

### 🎯 Goal
Enable job seekers to check their fit

### ✅ Tasks
- Upload resume → extract skills
- Show job matches
- Show skill gaps + suggested learning

### 🎁 Deliverable
- Basic employee UI experience

---

## 📊 Phase 13 — Insights & Analytics

### 🎯 Goal
HR intelligence dashboards

### ✅ Tasks
- Skill heatmaps
- Bench forecasting
- Career path visualization

### 🎁 Deliverable
- Insights dashboards in UI

---

## 🎯 Definition of Done (for every phase)
✅ Code + tests  
✅ CI pipeline passes  
✅ Docs updated  
✅ Demo working  

---

## 🌟 Summary Timeline

| Phase | Deliverable |
|---|---|
0 | Repo, CI, Walking Skeleton  
1 | DB + Read APIs  
2 | CLI Matcher (Rule‑Based)  
3 | Match API  
4 | Resume → Skills  
5 | Embeddings + Semantic Search  
6 | Evaluation + MLflow  
7 | Auth + RBAC  
8 | HR Web UI  
9 | Resume RAG Chat  
10 | Monitoring & Drift  
11 | CI/CD Release Pipeline  
12 | Employee Portal MVP  
13 | Analytics  

---

## 🚀 Next Step for You
Begin with **Phase 0 & 1**: repo structure, DB schema, API contracts, CI ready.

Reply when you're ready to start Phase 0 and I'll generate:

✅ Folder skeleton  
✅ Initial FastAPI code  
✅ CLI stub  
✅ Makefile  
✅ Pre‑commit hooks  
✅ CI workflow YAML  
✅ Seed data starter  

Let's build this like a real production system. 💪
