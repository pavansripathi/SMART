# ✅ SMART — Skill Mapping & AI-Driven Resource Tracking
> **Full-Stack + AI + MLOps End-to-End Learning Project**

SMART is an AI-powered Talent Intelligence platform that helps organizations
**discover, assess, match, and develop talent** using Machine Learning, LLMs, embeddings,
skill-graphs, and robust MLOps pipelines.

It also empowers **employees** to explore roles,
measure job fit, identify skill-gaps, and receive AI-driven learning paths.

This system is built as a **real-world enterprise project** to master:
- AI/NLP/Embeddings + RAG
- Full-stack system architecture
- MLOps lifecycle (data → train → deploy → monitor → retrain)
- Secure scalable backend engineering

---

## 🎯 Objectives

| Category | Focus |
|---|---|
AI | Resume parsing → embeddings → skill graph → talent scoring → recommendations  
MLOps | DVC, MLflow, Docker, CI/CD, Monitoring, retraining pipelines  
Full Stack | FastAPI backend, DB, Auth, UI (Streamlit → React)  
Security | JWT, RBAC roles, hashing, secret mgmt, audit logs  
Product | Employer + Employee talent ecosystem  

---

## 🚀 Key Features

### ✅ Employer / HR Portal
- Employee database & skills inventory
- Resume parsing + automatic skill extraction
- Semantic talent matching (project → people)
- Natural language HR chatbot:  
  *“Find React devs with 4+ yrs in Hyderabad available next 2 weeks”*
- Candidate ranking + shortlist flow
- Interview question generator (role-based)
- Chat with candidate resume (RAG)
- Bench usage + skill heatmap dashboard

### ✅ Employee Portal
- Job match scoring & ranking insights
- Comparison vs other applicants
- Skill-gap analysis & learning roadmap
- Resume bullet generator + ATS optimization
- AI mock interview assistant (future)

---

## 🧠 AI Modules

| Module | Purpose | Tools |
|---|---|---|
Resume Extraction | Identify skills, roles, years | spaCy / transformers  
Embeddings | Vectorize profiles & jobs | sentence-transformers / OpenAI  
Vector Search | Talent similarity search | FAISS / Qdrant  
Skill Graph | Skill relationships & hierarchy | NetworkX / Neo4j  
Match Scoring | Weighted talent-fit engine | Python pipeline  
RAG Resume Chat | AI answers about candidate profile | LangChain + vector DB  
Career Path Engine | Predict career trajectory | Embeddings + heuristics  
Learning Recommender | Suggest skills/courses | LLM + rule engine  

---

## 🏗️ Architecture

```
Frontend (Streamlit -> React UI)
        │
        ▼
FastAPI Backend ── JWT/RBAC ── ML Services
        │
 ┌──────┴──────────┐
 │                 │
SQL DB         Vector DB (FAISS/Qdrant)
 │                 │
DVC Data      MLflow Models & Registry
```

---

## 📦 Tech Stack

| Layer | Technology |
|---|---|
UI | Streamlit (MVP) → React + Tailwind  
API | FastAPI  
DB | SQLite (MVP) → PostgreSQL  
Auth | JWT, bcrypt, RBAC  
Vector DB | FAISS / Qdrant  
NLP | spaCy, Transformers  
LLM | OpenAI / HF + LangChain  
MLOps | DVC, MLflow, Prefect/Airflow  
DevOps | Docker, GitHub Actions  
Monitoring | Grafana, Prometheus, EvidentlyAI  

---

## 📂 Folder Structure

```
SMART/
├── backend/
│   ├── api.py                # FastAPI server
│   ├── auth/                 # JWT, RBAC, hashing
│   ├── core/                 # business logic (CRUD + matching)
│   ├── ml/                   # embedding + models
│   ├── rag/                  # chat with resumes
│   ├── data/                 # database + datasets
│   ├── tests/                # unit tests
│   └── Dockerfile
│
├── streamlit_ui/
│   └── app.py                # MVP UI
│
└── web_ui/ (future React client)
```

---

## 🧪 API Endpoints (MVP)

### Base URL
```
http://127.0.0.1:8000
```

| Method | Endpoint | Function |
|---|---|---|
GET | `/` | Health check |
POST | `/auth/login` | JWT login |
GET | `/employees` | List employees |
GET | `/employees/{id}` | Employee details |
POST | `/match` | Match candidate to job role |
POST | `/resume/extract` | Parse skills from resume |
POST | `/query/hr-agent` | HR chatbot |

---

## 📊 Talent Scoring Formula

```
TalentFit Score =
0.45 * Skill Match +
0.25 * Experience +
0.15 * Availability +
0.10 * Location/Domain Fit +
0.05 * Behavioral/Interview Score (future)
```

---

## 🧬 MLOps Lifecycle

| Stage | Tool | What it Covers |
|---|---|---|
Data versioning | DVC | Raw resumes, profiles, JDs, labels  
Experiment tracking | MLflow / W&B | Metrics, params, artifact storage  
Model registry | MLflow | Versioning, stage transitions (Staging/Prod)  
Feature store | Parquet / Redis (future) | Reusable features for inference  
Orchestration | Prefect / Airflow | ETL → Train → Evaluate → Deploy  
Containerization | Docker | Immutable deployments (API + workers)  
CI/CD | GitHub Actions | Lint, test, build, push images, deploy  
Monitoring | EvidentlyAI + Grafana | Data drift, performance, latency  
Auto-retrain | Cron / drift triggers | Re-train when drift/perf degrades  

---

## 🔐 Security

- bcrypt password hashing
- JWT access + refresh tokens
- RBAC (Admin / HR / Manager / Employee)
- `.env` secret config and least-privilege DB roles
- PII minimization (store only necessary fields)
- Audit logs for assignment & search actions

---

## ▶️ Running Locally

### 1) Install
```bash
pip install -r requirements.txt
```

### 2) Run Backend
```bash
uvicorn backend.api:app --reload
```

### 3) Run UI
```bash
streamlit run streamlit_ui/app.py
```

---

## 🧭 Development Roadmap

| Stage | Status |
|---|---|
Backend MVP + API | ✅  
Streamlit UI | ✅  
Resume parsing + embeddings | 🚧  
Semantic matching engine | 🚧  
LLM resume assistant | 🔜  
Vector DB + MLflow + DVC | 🔜  
React UI | 🔜  
CI/CD + monitoring | 🎯  

---

## 🤝 Contributing
This is a learning-focused, production-style project.  
Pull requests, architecture suggestions & feedback welcome!

---

## 🥅 Final Goal
Build a **real-world enterprise AI system** & master:

✔ Software engineering  
✔ AI systems & embeddings  
✔ MLOps & deployment  
✔ Database + Auth + RBAC  
✔ UI + APIs + DevOps pipelines

Not just "build an app", but learn how companies build **AI products at scale**.
