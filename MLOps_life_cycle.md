# High level (layman version)

* Client requirement
* Data Engineering (types of schema, multiple data sources for example vector DB, unstructured data to structurted data) - End result is gathered raw data (Bronze layer data) - for example pdfs excel files
* Data modeling - Planning a skeleton structure
* Data science - Silver (more structured) and gold layer (only data which is useful for our model)
* AI Engineering - Model selection, building, unit testing, MLOps - experimentation, tracking, logging
* Operationalizing - CI/CD starts here, QA, productionalizing
* Deployment and Maintainance in production (Continoius monitoring, feedback loops, drift analysis, model registring and model serving, inference - streaming, batch)


emp id, separate tables, 
db diagrams, er diagrams, entity relatios, - useful in data modeling stage

---

# High level (keyworded)

* __Business & Problem Framing:__
(client requirements, success metrics, constraints, ROI, stakeholders, use cases, risks, ethics & privacy, compliance)

* __Data Engineering (Ingest & Lake/Lakehouse):__
(sources: RDBMS, data lake/object store, APIs, logs, message queues, files—CSV/Parquet/JSON, PDFs/images/audio; schema-on-read vs schema-on-write; CDC; batch/stream; orchestration: Airflow/Dagster; Bronze = raw immutable; governance: catalog, lineage, access control)

* __Data Modeling (Data design, not ML):__
(conceptual/logical/physical models; star/snowflake; partitioning; table contracts; quality rules; PII handling; Lakehouse tables: Delta/Iceberg/Hudi)

* __Data Preparation & Feature Engineering (Silver/Gold):__
(EDA, cleaning, joins, normalization, imputations; dedup; label creation; feature pipelines; feature store; Gold = curated, analytics/ML-ready; data quality tests; sampling/splits; imbalance handling)

* __ML/AI Development (Data Science):__
(baselines, algorithm selection, training/validation/test splits; metrics; cross-validation; hyperparameter tuning; embeddings & vectorization (if RAG); responsible AI: bias/fairness, explainability; notebooks ↔ scripts; reproducibility/seeds)

* __AI/ML Engineering & MLOps (Build & Track):__
(training pipelines, experiment tracking, model registry, artifacts, versioning, data & model cards; unit/integration tests; evaluation suites; reproducible environments; dependency pinning; hardware utilization; privacy-preserving techniques)

* __Operationalization (CI/CD/CT):__
(containerization, IaC, CI for code + data tests, CD for services, CT = continuous training; approval gates; secrets management; blue-green/canary/shadow; A/B tests; rollback strategy)

* __Serving & Inference:__
(batch, real-time/online, streaming; REST/gRPC; feature store online/offline parity; vector DB for retrieval (FAISS/PGV/Weaviate/Milvus) in RAG; caching; autoscaling; cost control; latency & throughput SLAs)

* __Monitoring & Feedback Loops:__
(data/feature drift, concept drift, performance monitoring, data quality SLAs, logs/traces/metrics; alerting; human-in-the-loop review; feedback labeling; retraining triggers; incident playbooks)

* __Maintenance & Governance:__
(model lifecycle mgmt, deprecation, retrain schedules, documentation/model cards, access reviews, security, compliance, cost monitoring, postmortems, roadmap/backlog)

* __What is this called “officially”?__
The umbrella term is Machine Learning Lifecycle or MLOps Lifecycle.
A widely recognized framework you can map to is CRISP-DM (Business Understanding → Data Understanding → Data Preparation → Modeling → Evaluation → Deployment). Many teams extend CRISP-DM with MLOps (monitoring, retraining, CI/CD/CT).



    Also I want to do this in phases, the real CI/CD way. like for example in the first phase, getting everything ready like the project structure, gather required datasets, api end points, databse setup etc.. 

    and in the nexxt phase I want to develop a command line bases solution that works in the employer perspective with static inputs, like the skills and competency levels, experience, location and the result should be able to display a table of top matching candidates. 

    like wise, I want to build this in multiple but small and doable phaases. Please divide the entire project into sub tasks and give me the plan. let's do it piece by piece. and what do they call this type of project building, the technical term? 
