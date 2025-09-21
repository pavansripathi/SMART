from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Employee(Base):
    # create columns in the db
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    experience = Column(Integer, nullable=False)
    location = Column(String, nullable=False)
    salary = Column(String, nullable=False)
    skills = Column(String, nullable=False) # Storing JSON strings for now
