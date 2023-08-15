import os
import sqlalchemy
from sqlalchemy import create_engine,text

connection_str = os.environ["DB_CONNECTION_STR"]

engine = create_engine(
    connection_str,
    connect_args={
        "ssl": {
            "ca": "/etc/ssl/certs/ca-certificates.crt"
        }
    }
)
JOBS={}
id = ''
title = ''
company = ''
location = ''
responsibility = ''
requirement = ''
def db_job():
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
    all_jobs = result.all()
    
    for items in all_jobs:
      id = items[0]
      title = items[1]
      company = items[2]
      location = items[3]
      responsibility = items[4]
      requirement = items[5]
  JOBS={'id': id,'Title': title,'Company': company,'Location': location,'Responsibilities': responsibility,'Requirements':requirement}
  return JOBS

