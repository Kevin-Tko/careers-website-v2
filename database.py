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

def db_job():
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
    all_jobs = result.all()
    
    for items in all_jobs:
      JOBS={'id': items[0],'Title': items[1],'Company': items[2],'Location': items[3],'Responsibilities': items[4],'Requirements':items[5]}
    return JOBS

