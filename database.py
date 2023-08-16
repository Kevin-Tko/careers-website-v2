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
JOBS = []
def db_job():
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
    all_jobs = result.all()

    JOBS = [{'Id': item[0],'Title': item[1],'Company': item[2],'Location': item[3],'Duties': item[4],'Requirements': item[5]} for item in all_jobs]

    # for item in all_jobs:
    #   JOBS.append({
    #     'Id': item[0],
    #     'Title': item[1],
    #     'Company': item[2],
    #     'Location': item[3],
    #     'Duties': item[4],
    #     'Requirements': item[5]
    #   })

  return JOBS