from datetime import datetime
from dotenv import load_dotenv, main
import os
import csv
from client import InfluxClient
load_dotenv()
token  = os.getenv('TOKEN')
org    = os.getenv('ORG')
bucket = os.getenv('BUCKET')



IC = InfluxClient(token,org,bucket)

#IC.write_data(["MSFT,stock=MSFT Open=62.79,High=63.84,Low=62.13"])

query1 = 'from(bucket: "tse")\
|> range(start: 1633124983)\
|> filter(fn: (r) => r._field == "High")\
|> filter(fn: (r) => r.stock == "MSFT")'
IC.query_data(query1)