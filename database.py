import sqlalchemy
from sqlalchemy import text

print(sqlalchemy.__version__)

engine = sqlalchemy.create_engine("mysql+mysqlconnector://98m0kkn8lto6n768z161:pscale_pw_JPu3QhEXzb9GyLwtiAoxtcjtSHQdBv3pjHIhD0b4F7S@aws.connect.psdb.cloud:3306/careerswebsitev2")

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
