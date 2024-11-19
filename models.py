from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
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

# Create the tables
Base.metadata.create_all(engine)