# ✅ SMART — Skill Mapping & AI-Driven Resource Tracking

> **Full-Stack + AI + MLOps End-to-End Real-World Engineering System**

SMART is an enterprise-grade AI Talent Intelligence Platform built to learn and master:

* ✅ AI/ML + NLP + Embeddings
* ✅ Real-world MLOps lifecycle
* ✅ Full-stack engineering & DevOps
* ✅ Scalable backend + production CI/CD
* ✅ HR & Employee talent recommendation workflows

This is not a toy demo — this is a **serious, production-oriented learning product**.

SMART helps:

* **Employers** find & evaluate talent using AI
* **Employees** benchmark themselves & get skill-gap insights
* **Developers (us)** build a real SaaS-like system & master AI engineering

---

## 🎯 High-Level Objectives

| Category       | Outcome                                                                    |
| -------------- | -------------------------------------------------------------------------- |
| AI & ML        | Resume parsing → skill extraction → embeddings → scoring → recommendations |
| MLOps          | Training → evaluation → deployment → monitoring → retraining pipelines     |
| Full-Stack     | FastAPI backend, Streamlit/React UI, CLI, DB, Auth                         |
| DevOps         | Docker, CI/CD, GitHub Actions, environments                                |
| Security       | JWT, RBAC, hashing, audit logs                                             |
| Product Vision | Enterprise Talent Intelligence + Employee Career Assistant                 |

---

## 🚀 Key Platform Capabilities

### ✅ Employer / HR Portal

* Employee database & search
* Resume parsing → skill extraction
* Talent match scoring (Rule-based & ML)
* Salary prediction (ML regression)
* Rank & shortlist candidates
* Resume RAG chatbot
* Bench usage & skill heatmaps
* AI interview question generator
* Exportable reports

### ✅ Employee Portal

* Upload resume → extract skills
* Job fit score & ranking insights
* Skill-gap analysis
* Personalized learning roadmap
* Compare vs peer benchmark
* Resume improvement suggestions (ATS-optimized)

---

## 🧠 AI & ML Modules (High-Level)

| Module                           | Purpose                           |
| -------------------------------- | --------------------------------- |
| EDA + Data Prep                  | Understand talent/resume data     |
| Linear Regression                | Salary prediction v1              |
| Logistic Regression + Tree Model | Talent match scoring v1           |
| K-Means Clustering               | Skill segmentation                |
| TF-IDF NLP                       | Resume skills extraction baseline |
| KNN / Cosine Similarity          | Talent recommendations            |
| Resume RAG                       | Chat with candidate profiles      |
| Future: BERT + Vector DB         | Semantic candidate matching       |
| Future: ANN / LSTM               | Advanced resume modeling          |

---

## 🏗️ System Architecture (Top-Level)

```
Frontend (Streamlit → React)
        │
        ▼
FastAPI Backend ── Auth ── ML Services ── Vector Search
        │
 ┌──────┴──────────┐
 │                 │
SQL DB         Vector DB (Qdrant / FAISS)
 │                 │
Local + Cloud Storage for Datasets & Models
```

---

## 📦 Technology Stack

| Layer      | Tools                                                       |
| ---------- | ----------------------------------------------------------- |
| Frontend   | Streamlit (MVP) → React + Tailwind                          |
| Backend    | FastAPI + SQLAlchemy                                        |
| ML         | scikit-learn, sentence-transformers, spaCy                  |
| Vector DB  | Qdrant / FAISS                                              |
| Auth       | JWT + bcrypt + RBAC                                         |
| DB         | SQLite → PostgreSQL                                         |
| DevOps     | Docker, GitHub Actions                                      |
| MLOps      | Model artifacts, retraining workflows (future MLflow / DVC) |
| Monitoring | Prometheus, Grafana, EvidentlyAI (later phases)             |

---

## 📂 Repository Structure (High-Level)

```
SMART/
├── backend/           # FastAPI backend & ML services
├── cli/               # SMART CLI utilities
├── data/              # Raw datasets & seeds
├── docs/              # Deep technical & learning docs
├── ui/                # Streamlit → React Frontend
└── .github/workflows/ # CI/CD pipelines
```

---

## 🧪 Quality & Testing

* ✅ Unit tests (pytest)
* ✅ Linting (ruff, black, isort)
* ✅ GitHub Actions CI
* ✅ Docker parity dev environment
* 🔜 UI testing (Playwright/Selenium)
* 🔜 ML evaluation tests & performance checks

---

## 🔐 Security Principles

* JWT + RBAC roles
* Encrypted secrets via `.env`
* Audit logging for sensitive events
* Minimal data retention & PII safety

---

## 🚦 Development Roadmap Snapshot

| Phase    | Focus                                 |
| -------- | ------------------------------------- |
| Phase 0  | ✅ Repo, CI, Docker, CLI, health check |
| Phase 1  | DB + Seed data + Read API             |
| Phase 2  | EDA + feature engineering             |
| Phase 3  | CLI matching (rule-based)             |
| Phase 4  | Salary ML model & API                 |
| Phase 5  | ML-based match engine                 |
| Phase 6  | Clustering engine                     |
| Phase 7  | Resume skill extraction NLP           |
| Phase 8  | Recommendation engine                 |
| Phase 9  | Full HR UI                            |
| Phase 10 | Auth + RBAC                           |
| Phase 11 | Resume RAG chat                       |
| Phase 12 | Analytics dashboards                  |
| Phase 13 | Employee portal                       |
| Phase 14 | Monitoring & drift                    |
| Phase 15 | CI/CD deployment pipeline             |

🔁 **Version 1.1.0 & 1.2.0 add advanced ML, embeddings, deep learning & full MLOps**

> Full phase roadmap lives in `docs/phase_wise_plan.md`

---

## ▶️ Quick Start

```bash
# Create venv
python -m venv .venv

# Activate
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

# Install deps
pip install -r backend/requirements.txt

# Run API
uvicorn backend.app:app --reload

# Run UI (MVP)
streamlit run ui/app.py
```

---

## 🥅 Final Vision

Build a real AI Talent Intelligence SaaS:

* Real-world AI
* Real-world DevOps
* Real-world MLOps
* Real-world UI/UX

**Not just learning — building professional software.**
