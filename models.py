from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, func
from database import engine

Base = declarative_base()

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    location = Column(String, nullable=False)
    salary = Column(Integer)
    currency = Column(String)
    responsibilities = Column(String)
    requirements = Column(String)

class Application(Base):
    __tablename__ = 'applications'
    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    linkedin_url = Column(String, nullable=False)
    education = Column(String, nullable=False)
    work_experience = Column(String, nullable=False)
    resume_url = Column(String, nullable=False)

# Create the tables
Base.metadata.create_all(engine)