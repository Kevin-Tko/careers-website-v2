import sqlalchemy
from sqlalchemy import text

print(sqlalchemy.__version__)

password = 'm15zubn5xoypaw36ov15'
username = 'pscale_pw_A7KqYUK0cF2pgtHKmt9FCgXdYyQKNrBqPU2erNqQQqy'
host = 'aws.connect.psdb.cloud'
db = 'careerswebsitev2'
port = '3306'

engine = sqlalchemy.create_engine(f"mysql+mysqlconnector://{password}:{username}@{host}:{port}/{db}")

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
jobs_listing = db_job()
# print(jobs_listing)
