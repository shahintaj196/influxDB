from datetime import datetime
from dotenv import load_dotenv, main
import os
import csv
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS, ASYNCHRONOUS

load_dotenv()
token  = os.getenv('TOKEN')
org    = os.getenv('ORG')
bucket = os.getenv('BUCKET')
client = InfluxDBClient(url="http://localhost:8086", token=token)


class InfluxClient:
    def __init__(self,token,org,bucket): 
        self._org    = org 
        self._bucket = bucket
        self._client = InfluxDBClient(url="http://localhost:8086", token =token)
    
    def write_data(self,data,write_option=SYNCHRONOUS):
        write_api = self._client.write_api(write_option)
        write_api.write(self._bucket, self._org , data,write_precision='s')
    
    def query_data(self,query):
        query_api = self._client.query_api()
        result = query_api.query(org=self._org, query=query)
        results = []
        for table in result:
            for record in table.records:
                results.append((record.get_value(), record.get_field()))
        print(results)
        return results
    
    def delete_data(self,measurement):
        delete_api = self._client.delete_api()
        start = "1970-01-01T00:00:00Z"
        stop = "2021-10-30T00:00:00Z"
        delete_api.delete(start, stop, f'_measurement="{measurement}"', bucket=self._bucket, org=self._org)


IC = InfluxClient(token,org,bucket)


MSFT_file = open('FINANCE.csv')
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
IC.write_data(["MSFT,stock=MSFT Open=62.79,High=63.84,Low=62.13"])

query1 = 'from(bucket: "tse")\
|> range(start: 1633124983)\
|> filter(fn: (r) => r._field == "High")\
|> filter(fn: (r) => r.stock == "MSFT")'
IC.query_data(query1)
query2 = 'from(bucket: "tse")\
|> range(start: 1633124983)\
|> filter(fn: (r) => r._field == "High")\
|> filter(fn: (r) => r._measurement == "MSFT_2021-10-29")'

IC.query_data(query2)