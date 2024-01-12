from datetime import datetime
from dotenv import load_dotenv, main
import os
import csv
from .c
load_dotenv()
token  = os.getenv('TOKEN')
org    = os.getenv('ORG')
bucket = os.getenv('BUCKET')
client = InfluxDBClient(url="http://localhost:8086", token=token)


IC = InfluxClient(token,org,bucket)