import sqlalchemy
from sqlalchemy import text
import mysql
import mysql.connector

print(sqlalchemy.__version__)

password = 'cmjxuql4b3fmquhbrutu'
username = 'pscale_pw_86wZ3knbXCLNBnTXX7UQrfBgOowmfesN8MyQRkhmMST'
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
