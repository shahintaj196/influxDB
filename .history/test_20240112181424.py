from datetime import datetime
from dotenv import load_dotenv, main
import os
import csv
from .clinet import InfluxClient
load_dotenv()
token  = os.getenv('TOKEN')
org    = os.getenv('ORG')
bucket = os.getenv('BUCKET')



IC = InfluxClient(token,org,bucket)