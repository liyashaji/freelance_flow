from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Graphics Designer',
        'salary': 'Rs.1000 pw'
    },
    {
        'id': 2,
        'title': 'UI/UX designer',
        'salary': 'Rs.5000 pw'
    },
    {
        'id': 3,
        'title': 'Guitar Teacher',
        'salary': 'Rs.7000'
    },
    {
        'id': 4,
        'title': 'Web Developer',
        'salary': 'Rs.5000'
    },
    {
        'id': 5,
        'title': 'App Developer',
        'salary': 'Rs.10000'
    }
]

@app.route("/")
def hello_freelance():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify (JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
