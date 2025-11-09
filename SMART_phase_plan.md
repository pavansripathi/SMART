# SMART Project Roadmap — Detailed Phases (v1.0.0)

This plan includes **all original features** + newly added ML modules, automated testing strategies, MLOps lifecycle alignment, and full production scope.

> Building SMART like a real enterprise Talent Intelligence Platform — not a toy.

---

## ✅ Phase 0 — Project Bootstrap (Walking Skeleton)

**Goal:** Establish foundation + CI + DevOps hygiene

### Tasks

* Create monorepo structure
* Initialize Git repo & branch strategy
* Add FastAPI skeleton with `/health` endpoint
* CLI bootstrap (`smart` command placeholder)
* Testing: pytest installed + basic smoke test
* Code quality tooling:

  * black, ruff, isort, pre‑commit hooks
* Dockerfile + docker‑compose
* GitHub Actions CI (lint + tests on push/PR)

### Performance / Quality Metrics

* ✅ CI must pass for every commit
* ✅ Pre‑commit auto‑format enforced
* ✅ Lint score: `ruff check .` clean
* ✅ Test coverage: basic (smoke only)

### Output

* Running backend & CLI
* CI pipelines green
* Dev environment reproducibility ensured

---

## 📊 Phase 1 — Data Schema, Seed, Basic API

**Goal:** Data design + first working endpoints

### Tasks

* DB schema design (employees, skills, mapping table)
* Alembic migrations setup
* Seed data in CSV/XLSX + loader
* API Endpoints:

  * `GET /employees`
  * `GET /employees/{id}`
* Add dataclasses / Pydantic models
* Unit tests for DAO + endpoints

### Metrics

* ✅ Test coverage > 50%
* ✅ DB migrations successful end‑to‑end
* ✅ Seed load reproducible

### Output

* CRUD foundation for ML features

---

## 🧠 Phase 2 — EDA & Feature Engineering Prep

**Goal:** Understand data and prep for ML

### Tasks

* Data profiling (distribution, variance, missing values)
* Outlier detection
* Encoding: One‑Hot / Label encoding
* Scaling for numeric features
* Feature store structure
* Notebook for EDA

### Metrics

* ✅ EDA report documented
* ✅ Cleaned dataset ready
* ✅ Feature pipeline functions created

### Output

* ML‑ready data pipeline

---

## 💻 Phase 3 — CLI MVP (Rule‑Based Matching)

**Goal:** Offline matching baseline

### Tasks

* CLI: `smart match --skills ... --top-k X`
* Rule‑based score function
* Table/CSV output
* Unit tests

### Metrics

* ✅ CLI user experience smooth
* ✅ Confident baseline for ML comparison

### Output

* First working matching system

---

## 🤖 Phase 4 — Salary Prediction Model (Regression v1)

**Goal:** Baseline model & deployment

### Tasks

* Split train/test
* Train Linear Regression model
* Evaluate: MAE, MSE, RMSE, R²
* Save trained model artifact
* FastAPI route: `POST /salary/predict`
* Unit test on model input/output

### Metrics

* RMSE threshold defined
* Model inference <100ms
* Test coverage >65%

### Output

* Salary predictor v1 deployed

---

## 🎯 Phase 5 — ML‑Based Skill Match (Classification v1)

**Goal:** Replace rule logic with simple ML classifier

### Tasks

* Train Logistic Regression
* Compare with Decision Tree
* Metrics: Precision, Recall, F1
* Explainability (Tree viz)
* Endpoint: `POST /match/ml`
* Config flag: rule | ml
* Tests for ML output & scoring

### Metrics

* F1 > rule‑based baseline
* Explainable predictions

### Output

* ML match engine v1

---

## 🧩 Phase 6 — Skill Clustering Engine

**Goal:** Group similar employees

### Tasks

* K‑Means clustering
* Silhouette score baseline
* Visual output saved to /plots
* Endpoint: `GET /clusters`

### Metrics

* Silhouette score tracked

### Output

* Employee skill clusters

---

## 📝 Phase 7 — Resume Skill Extraction (NLP v1)

**Goal:** Extract skills from CV text

### Tasks

* TF‑IDF vectorization
* Tokenization + stopwords + lemmatization
* Endpoint: `POST /resume/skills`
* Test text extraction

### Metrics

* Extraction accuracy baseline documented

### Output

* Basic resume parser

---

## 🔍 Phase 8 — Recommendation Engine

**Goal:** Find similar employees or jobs

### Tasks

* KNN / cosine similarity
* `GET /recommend/employees`, `/jobs`
* Write evaluation notebook

### Metrics

* Response <150ms

### Output

* Recommender v1

---

## 🌐 Phase 9 — HR Console UI

**Goal:** Full web UI for HR users

### Tasks

* Web UI (Streamlit or React)
* Pages:

  * Login
  * Employee explorer
  * Salary predictor
  * Match engine
  * Clusters
  * Resume parser
  * Recommendations
* UI tests: Selenium/Playwright

### Metrics

* UI load <2s
* Selenium smoke suite passes

### Output

* ✅ Full HR user interface

---

## 🔐 Phase 10 — Auth + RBAC

**Goal:** Security and compliance

### Tasks

* JWT auth
* User roles (Admin/HR/Manager)
* Audit logs
* Protected endpoints

### Output

* Secure platform access

---

## 💬 Phase 11 — Resume RAG Chat

**Goal:** Chat with candidate data

### Tasks

* Embed resume chunks
* Retrieval + prompt chain
* Endpoint + UI chat

### Output

* Interactive resume chat

---

## 📈 Phase 12 — Analytics & Insights

**Goal:** HR dashboards

### Tasks

* Skill heatmaps
* Salary bands
* Top skills gaps
* Model accuracy dashboards

### Output

* Insight UI pages

---

## 👤 Phase 13 — Employee Portal

**Goal:** Candidate self‑service portal

### Features

* Upload resume → skills
* Skill gap & suggestions
* Compare with job benchmarks

### Output

* Employee‑facing UI

---

## 🛰️ Phase 14 — Monitoring & Drift

**Goal:** Observability + ML drift detection

### Tasks

* Prometheus + Grafana
* EvidentlyAI
* Alerts on drift

### Output

* ML monitoring pipeline

---

## 🚚 Phase 15 — CI/CD Release & Deployment

**Goal:** Auto deploy to cloud

### Tasks

* Multi‑stage Docker build
* GitHub Actions release
* Version tagging
* Blue‑green / rolling deploys

### Output

* Auto build + deploy on merge to main

---

> **End result:** A real production Talent Intelligence System with ML, RAG, UI, security, CI/CD, and monitoring.

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

---

## 📌 Version Summary Table

| Version | Theme | Highlights |
|---|---|---|
**1.0.0** | Core Product + Core ML | UI, salary model, match model, clustering, TF-IDF NLP, recsys, RAG, employee portal, analytics, CI/CD |
**1.1.0** | ML + UX Enhancements | RF/XGBoost, SHAP, spaCy NER, SMOTE, dashboards, exports, model tuning |
**1.2.0** | Advanced AI + MLOps | BERT, Vector DB, ANN/LSTM, MLflow, forecasting, canary deploys |
