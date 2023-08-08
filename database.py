# import os
import sqlalchemy
from sqlalchemy import create_engine,text

# host = os.environ["HOST"]
# user = os.environ["USERNAME"]
# password = os.environ["PASSWORD"]
# dbname = os.environ["DATABASE"]
# print(host)

connection_str = 'mysql+pymysql://o3190r2rfm0od1xoun2q:pscale_pw_5hR8pCJ7cjU9501FXlXNdKLXdzXqF2oFMxKXvLfYejh@aws.connect.psdb.cloud/careerswebsitev2?charset=utf8mb4'

# ssl_args = {
#   'ssl_ca':"/etc/ssl/cert.pem"
# }
engine = create_engine(
    connection_str,
    connect_args={
        "ssl": {
            "ca": "/etc/ssl/certs/ca-certificates.crt"
        }
    }
)

# engine = create_engine(connection_str, connect_args=ssl_args)

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

