# import os
import sqlalchemy
from sqlalchemy import create_engine,text

# host = os.environ["HOST"]
# user = os.environ["USERNAME"]
# password = os.environ["PASSWORD"]
# dbname = os.environ["DATABASE"]
# print(host)

connection_str = 'mysql+pymysql://88cwrdv2659ospeog4hh:pscale_pw_l1iaWIuU4rJLQVyc3lnDayAzarBfcE6M4oHMeI0yC96@aws.connect.psdb.cloud/careerswebsitev2?charset=utf8mb4'

engine = create_engine(connection_str, echo=True)

JOBS=[]
def db_job():
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
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

