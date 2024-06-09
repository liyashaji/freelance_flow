from flask import Flask
from flask import render_template
from flask import jsonify
from database import engine
from sqlalchemy import text
from dotenv import load_dotenv
import os

load_dotenv() 
app = Flask(__name__)

app.config['DEBUG'] = True

def load_jobs_from_db():
     try:
        with engine.connect() as conn:
            # Create a text object for the SQL query
            query = text("select * from jobs")
            
            # Execute the query
            result = conn.execute(query)
            
            # Get the column names
            column_names = [desc[0] for desc in result.cursor.description]
            
            # Convert the result rows to dictionaries
            jobs = [dict(zip(column_names, row)) for row in result]
            
            return jobs
     except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")



@app.route("/")
def hello_freelance():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify (jobs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
