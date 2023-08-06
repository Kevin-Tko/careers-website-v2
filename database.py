import sqlalchemy as sql
from sqlalchemy import text

engine = sql.create_engine("mysql+mysqlconnector://67fvk2naiow4i2a9ylbf:pscale_pw_bREuGTkd2JTDKWSldHBKNzlgZeUj47YUG1FWn8bDKFk@aws.connect.psdb.cloud:3306/careerswebsitev2")

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
