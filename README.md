**Name: SMART — Skill Mapping \& AI-driven Resource Tracking**

**Goal:** Help organizations find the right people quickly by mapping people → skills → availability and using AI to recommend best-fit resources and training.

Primary users: Delivery managers, People Ops, Team leads, Project managers.


**Core capabilities (MVP):**

Central employee DB (skills, experience, availability, assignments)

Skill normalization \& extraction (from CVs, profiles, free text)

Semantic matching: project requirements → ranked candidate list

Quick demo GUI (Streamlit) + backend API (FastAPI)

Basic assignment flow (tentative assignment + confirmation)

Metrics: match-score, candidate shortlist, fill-rate (demo-level)


**Value / Use-cases:**

Faster resourcing: reduce time-to-fill

Better matches (skill + experience + availability)

Proactive bench utilization and upskilling recommendations

Audit trail for assignment decisions


**Privacy/security highlights (MVP) Minimum Viable Product:**

Store only necessary PII

use role-based access in production

Audit logs for assignment actions

Encrypt DB credentials and use least-privilege DB users


------------------------------------------------------------------------------


**This is the project structure**

SMART/
│
├── backend/
│   ├── api.py               # FastAPI entrypoint (uvicorn)
│   ├── db.py                # SQLite + SQLAlchemy setup
│   ├── core/
│   │   ├── employees.py     # CRUD logic
│   │   └── main.py          # AI/ML logic placeholder
│   ├── data/
│   │   └── smart.db
│   └── __init__.py
│
├── streamlit_ui/
│   └── app.py               # Streamlit GUI that imports backend/core directly
│
├── web_ui/                  # UI part
│   ├── package.json
│   ├── src/
│   └── public/
│
└── README.md
