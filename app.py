from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db
import os
from dotenv import load_dotenv

# load env variables
load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs)  

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/job/<int:id>")
def show_job(id):
    job = load_job_from_db(id)
    if job is None:
        return jsonify({"message": "Job doesn't exist"})
    return render_template('jobpage.html', job=job)

if __name__ == "__main__":
    app.run(debug= os.getenv('FLASK_ENV') == 'development')