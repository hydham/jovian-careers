from sqlalchemy import create_engine, text 
import os

basedir = os.path.abspath(os.path.dirname(__file__))
database_uri = f"sqlite+pysqlite:///{os.path.join(basedir, 'joviancareers.db')}"

engine = create_engine(database_uri, echo=True)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = [dict(row._mapping) for row in result.all()]
        return jobs


    




