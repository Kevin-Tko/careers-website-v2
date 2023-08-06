from database import db_job
from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder='static')


@app.route("/")
def hello_word():
  jobs_ls = db_job()
  return render_template('home.html', jobs=jobs_ls)

@app.route("/api/jobs")
def list_jobs():
  jobs_ls = db_job()
  return jsonify(jobs_ls)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)