# import os
from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder='static')

JOBS = [
  {
    'id': 1,
    'Title': 'Bank Teller',
    'Location': 'Nairobi',
    'Company': 'Standared Chartered Bank'
  },
  {
    'id': 2,
    'Title': 'Treasury Officer',
    'Location': 'Mombasa',
    'Company': 'Stanbic Bank'
  },
  {
    'id': 3,
    'Title': 'Service Desk Assistant',
    'Location': 'Remote',
  },
  {
    'id': 4,
    'Title': 'Credit Manager',
    'Location': 'Nairobi',
    'Company': 'ABC Bank'
  }
]


@app.route("/")
def hello_word():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)