import os
import sqlalchemy
from sqlalchemy import create_engine,text

host = os.environ["HOST"]
user = os.environ["USERNAME"]
password = os.environ["PASSWORD"]
dbname = os.environ["DATABASE"]
print(host)

connection_str = f'mysql+mysqlconnector://{user}:{password}@{host}:3306/{dbname}'

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
