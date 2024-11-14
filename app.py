from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {'title': 'Data engineer',
     'location': 'Banglore, India',
     'salary': 'Rs 10,00,000'},
     {'title': 'Data scientist',
     'location': 'Delhi, India',
     'salary': 'Rs 10,00,000'},
     {'title': 'Frontend Engineer',
     'location': 'Remote',
     'salary': '$ 60,000'},
]

@app.route("/")
def home():
    return render_template("home.html", jobs=JOBS)  

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)