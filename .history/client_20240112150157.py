from datetime import datetime
from dotenv import load_dotenv, main
import os
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS, ASYNCHRONOUS

load_dotenv()
# You can generate a Token from the "Tokens Tab" in the UI
token = os.getenv('TOKEN')
org = os.getenv('ORG')
bucket = os.getenv('BUCKET')

client = InfluxDBClient(url="http://localhost:8086", token=token)

def write_data(self,data,write_option=SYNCHRONOUS):
    write_api = self._client.write_api(write_option)
    write_api.write(self._bucket, self._org , data,write_precision='s')

class InfluxClient:
    def __init__(self,token,org,bucket): 
        self._org=org 
        self._bucket = bucket
        self._client = InfluxDBClient(url="http://localhost:8086", token=token)
      
      
        
IC = InfluxClient(token,org,bucket)

