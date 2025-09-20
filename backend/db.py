# SQLite + SQLAlchemy setup

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.core.employees import Base

engine = create_engine("sqlite:///backend/data/smart.db")
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
