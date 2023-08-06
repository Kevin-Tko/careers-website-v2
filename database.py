import sqlalchemy as db
from sqlalchemy import text

engine = db.create_engine("mysql+mysqlconnector://b59gm61vzjk5cbkqbgmi:pscale_pw_aSP9NskXdfIOqyYgfQFrkOU6prwg3PUleHkCH4wJJbG@aws.connect.psdb.cloud:3306/careerswebsitev2")

def db_job():
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
    JOBS=[]
    all_jobs = result.all()
    for items in all_jobs:
      JOBS.append({
        'id': items[0],
        'Title': items[1], 
        'Company': items[2],
        'Location': items[3],
        'Responsibilities': items[4],
        'Requirements':items[5]}
      )
    return JOBS