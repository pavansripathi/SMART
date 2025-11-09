# SMART Project Roadmap — Detailed Phases (v1.0.0)

This plan includes **all original features** + ML modules, automated testing strategies, MLOps alignment, DB clarity, ATS scoring, and security practices.

> Building SMART like a real enterprise Talent Intelligence Platform — not a toy.

---

## ✅ Phase 0 — Project Bootstrap (Walking Skeleton)

**Goal:** Establish foundation + CI + DevOps hygiene

### Tasks
- Create monorepo structure
- Initialize Git repo & branch strategy
- Add FastAPI skeleton with `/health` endpoint
- CLI bootstrap (`smart` command placeholder)
- pytest installed + basic smoke test
- Code quality:
  - black, ruff, isort, pre-commit hooks
- Dockerfile + docker-compose
- GitHub Actions CI (lint + tests)
- `.env` config + Pydantic settings module

### Performance / Quality Metrics
- ✅ CI must pass for every commit
- ✅ Pre-commit auto-format enforced
- ✅ Lint score: `ruff check .` clean
- ✅ Test coverage: smoke tests enabled

### DB & MLOps notes
- Postgres + SQLite dev fallback (Docker ready)
- Model folder structure + artifact dir initialized

### Output
- Working backend & CLI
- CI pipelines green
- Reproducible dev environment

---

## 📊 Phase 1 — Data Schema, Seed, Basic API

**Goal:** Data design + first working endpoints

### Tasks
- PostgreSQL schema (employees, skills, junction table)
- SQLite fallback for local dev
- Alembic migrations setup
- Seed data from CSV/XLSX
- API Endpoints:
  - `GET /employees`
  - `GET /employees/{id}`
- Pydantic models
- Unit tests for DB + API

### Metrics
- ✅ Test coverage > 50%
- ✅ DB migrations consistent
- ✅ Seed process reproducible

### Output
- CRUD foundation for ML features

---

## 🧠 Phase 2 — EDA & Feature Engineering Prep

**Goal:** Understand data and prep for ML

### Tasks
- EDA notebook
- Data cleaning + missing value handling
- Outliers & scaling
- One-hot / label encoding
- Feature pipeline utilities
- Store intermediate data versions

### Metrics
- ✅ EDA documented
- ✅ Feature functions created

### Output
- ML-ready data pipeline

---

## 💻 Phase 3 — CLI MVP (Rule-Based Matching)

**Goal:** Offline matching baseline

### Tasks
- CLI command: `smart match --skills ... --top-k`
- Rule-based scoring formula
- CSV + Table output
- Local config for weights
- CLI tests

### Metrics
- ✅ CLI UX smooth
- ✅ Baseline ready for ML comparison

### Output
- Rule-based matching working in CLI

---

## 🤖 Phase 4 — Salary Prediction Model (Regression v1)

**Goal:** Train & serve first ML model

### Tasks
- Train Linear Regression model
- MAE, RMSE, R² eval
- Save model artifact
- `/salary/predict`
- Unit tests for inference
- Logging inference performance

### Metrics
- RMSE threshold defined
- Inference <100ms
- >65% test coverage on model inputs

### Output
- Salary predictor v1 served via API

---

## 🎯 Phase 5 — ML-Based Skill Match (Classification v1)

**Goal:** Replace rule logic with ML baseline

### Tasks
- Logistic Regression baseline
- Decision Tree explainability
- Precision, Recall, F1, Confusion matrix
- `/match?mode=ml`
- Test ML output consistency

### Metrics
- F1 > rule-based baseline
- Explainability visual access

### Output
- ML match engine v1

---

## 🧩 Phase 6 — Skill Clustering Engine

**Goal:** Group similar talent profiles

### Tasks
- K-Means clustering
- Silhouette score
- Visualization saved to `/plots`
- `GET /clusters`

### Output
- Skill clusters visible in UI later

---

## 📝 Phase 7 — Resume Skill Extraction (NLP v1)

**Goal:** Extract skills from raw text

### Tasks
- Tokenization + stopwords + lemmatization
- TF-IDF baseline
- `/resume/skills`
- Unit tests for text parsing

### Output
- Basic resume parsing pipeline

---

## 🔍 Phase 8 — Recommendation Engine

**Goal:** Recommend employees & jobs

### Tasks
- KNN / cosine similarity
- `/recommend/employees`
- `/recommend/jobs`
- Evaluation notebook

### Output
- Talent recommendation v1

---

## 🌐 Phase 9 — HR Console UI

**Goal:** Full HR interface

### Pages
- Login page
- Employee browser
- Salary predictor
- ML matcher
- Skill clusters
- Resume parser
- Recommendations

### Testing
- ✅ UI tests (Playwright/Selenium)
- ✅ API integration tests

### Output
- HR platform UI operational

---

## 🔐 Phase 10 — Auth + RBAC

**Goal:** Enterprise-grade access control

### Tasks
- JWT auth
- RBAC roles (Admin/HR/Manager)
- **Audit logs for access + searches**
- Rate limits on sensitive endpoints

### Output
- Secure multi-role platform

---

## 💬 Phase 11 — Resume RAG Chat

**Goal:** Conversational talent search

### Tasks
- Embed resume chunks
- Retrieval chain
- `/resume/chat`
- UI chat widget

### Output
- RAG-powered resume Q&A

---

## 📈 Phase 12 — Analytics & Insights

**Goal:** HR dashboards

### Charts
- Skill heatmaps
- Salary ranges
- Hiring funnel stats
- Model performance charts

### Output
- Analytics UI pages

---

## 👤 Phase 13 — Employee Portal

**Goal:** Empower employees

### Features
- Upload resume → skills
- Job match score
- Peer comparison (privacy safe)
- **ATS optimization score**
- Skill-gap suggestions
- Learning pathways

### Output
- Employee portal online

---

## 🛰️ Phase 14 — Monitoring & Drift

**Goal:** System & model reliability

### Tasks
- Prometheus + Grafana dashboards
- EvidentlyAI drift checks
- Alerts on drift or degraded accuracy

### Output
- Real ML observability

---

## 🚚 Phase 15 — CI/CD & Deployment

**Goal:** Production deployment pipeline

### Tasks
- Multi-stage Docker builds
- GitHub Actions deploy
- Version tags + release notes
- Blue-green deployment
- Rollback strategy

### Output
- Continuous delivery to cloud

---

# ✅ End of v1.0.0 (Core System Delivered)

---

> **End of version 1.0.0** In the later versions we'll deliver more advanced features and improvements.

## 🚀 Version 1.1.0 — Enhancements & Model Upgrades

### 🎯 Focus
Strengthen ML performance, improve UX, introduce advanced ML concepts.

### ✅ ML Enhancements
- Add **Random Forest** for salary prediction
- Add **XGBoost** variant for match model
- Hyperparameter tuning (GridSearchCV / Optuna)
- Model leaderboard & comparison logs
- Explainability tools:
  - SHAP for salary model
  - Decision Tree visualization for match model

### ⚙️ Feature Engineering Upgrades
- SMOTE / Upsampling for class imbalance
- Advanced outlier handling
- Feature importance dashboard

### 🧪 Evaluation & Monitoring
- ROC / AUC curves
- Precision–Recall curve
- Confusion Matrix UI panel
- Threshold tuning UI

### 📝 Resume Parsing Improvements
- N-gram based extraction
- spaCy NER for skill identification
- Expanded skill & role dictionary

### 🖥️ UI Enhancements
- Enhanced theme & UX polish
- Saved searches & profile notes
- PDF & Excel export for reports
- Candidate comparison UI

### 🔐 Platform Improvements
- Refined role-based access
- Activity log viewer

---

## 🧠 Version 1.2.0 — Advanced AI & MLOps

### 🎯 Focus
Deep learning, semantic matching, vector search, production MLOps.

### 🤖 Deep Learning Models
- ANN salary model (Keras/PyTorch)
- Bi-LSTM resume sequence model
- Live training charts (loss & accuracy curves)

### 🧠 Advanced NLP & Semantic Talent System
- BERT embeddings for resumes & skills
- Hybrid scoring (keyword + ML + semantic)
- **Vector DB** (Chroma / Qdrant)
- Resume similarity search
- Skill gap inference & learning path suggestions

### 🧪 Advanced Ranking & Evaluation
- MAP@K, NDCG@K evaluation
- Benchmark suite for candidate ranking
- A/B experiment system for ML models

### 🛰️ MLOps Enhancements
- MLflow tracking + model registry
- Versioned model lifecycle (dev → staging → prod)
- Scheduled re-training pipeline

### 📉 Forecasting Capabilities
- Employee availability / bench prediction (ARIMA / LSTM)

### 🌐 Deployment & Reliability
- Canary deployments
- Auto rollback strategy
- Latency testing for ML inference

**Plus explicit items added:**
- ✅ Qdrant / pgvector integration
- ✅ Career Path Engine (graph inference)
- ✅ Optional Neo4j skill graph
- ✅ MLflow registry + retraining pipeline

---

## 📌 Version Summary Table

| Version | Theme | Highlights |
|---|---|---|
**1.0.0** | Core Product + Core ML | UI, salary model, match model, clustering, TF-IDF NLP, recsys, RAG, employee portal, analytics, CI/CD |
**1.1.0** | ML + UX Enhancements | RF/XGBoost, SHAP, spaCy NER, SMOTE, dashboards, exports, model tuning |
**1.2.0** | Advanced AI + MLOps | BERT, Vector DB, ANN/LSTM, MLflow, forecasting, canary deploys |
