from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db, list_applications
import os
from dotenv import load_dotenv
import models

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

@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Page not found", 404
    return render_template('jobpage.html', job=job)

@app.route("/job/<id>/apply", methods=['POST'])
def apply_job(id):
    job = load_job_from_db(id)
    data = request.form
    add_application_to_db(id, data)
    return render_template('application_submitted.html', 
                           data=data, 
                           job=job)

@app.route("/api/applications")
def show_applications():
    data = list_applications()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug= os.getenv('FLASK_ENV') == 'development')