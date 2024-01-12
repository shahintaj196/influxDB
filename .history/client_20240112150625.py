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


MSFT_file = open('Data/MSFT.csv')
csvreader = csv.reader(MSFT_file)
header = next(csvreader)
rows = []
for row in csvreader:
        date,open,high,low = row[0],row[1],row[2],row[3]
        line_protocol_string = ''
        line_protocol_string+=f'MSFT_{date},'
        line_protocol_string+=f'stock=MSFT '
        line_protocol_string+=f'Open={open},High={high},Low={low} '
        line_protocol_string+=str(int(datetime.strptime(date,'%Y-%m-%d').timestamp()))
        rows.append(line_protocol_string)

IC.write_data(rows)
# Data Write Method 1
# IC.write_data(["MSFT,stock=MSFT Open=62.79,High=63.84,Low=62.13"])

# Data Write Method 2
# IC.write_data(
# [
# Point('MSFT')
# .tag("stock","MSFT")
# .field("Open",62.79)
# .field("High",63.38)
# .field("Low",62.13)
# .time(int(datetime.strptime('2021-11-07','%Y-%m-%d').timestamp()))
# ],
# )

# Data Write Method 3
# IC.write_data([
# {
# "measurement": "MSFT",
# "tags": {"stock": "MSFT"},
# "fields": {
# "Open": 62.79,
# "High": 63.38,
# "Low": 62.13,
# },
# "time": int(datetime.strptime('2021-11-07','%Y-%m-%d').timestamp())
# },
# {
# "measurement": "MSFT_DATE",
# "tags": {"stock": "MSFT"},
# "fields": {
# "Open": 62.79,
# "High": 63.38,
# "Low": 62.13,
# },
# }
# ],write_option=ASYNCHRONOUS)