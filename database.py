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

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :val"), 
            {"val": id})
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0]._mapping)

def add_application_to_db(id, data):
    with engine.connect() as conn:
        transaction = conn.begin()
        try:
            query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
            conn.execute(query, 
                     {
                        "job_id": id, 
                        'full_name': data['full_name'], 
                        'email': data['email'], 
                        'linkedin_url': data['linkedin_url'], 
                        'education': data['education'], 
                        'work_experience': data['work_experience'],
                        'resume_url': data['resume_url']
                    })
            transaction.commit()
        except Exception as e:
            transaction.rollback()
            print("Error during insertion: ", e)
       

        
        
def list_applications():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM applications"))
        applications = [dict(row._mapping) for row in result.all()]
        return applications
    