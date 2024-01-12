from datetime import datetime
from dotenv import load_dotenv, main
import os
import csv
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS, ASYNCHRONOUS

load_dotenv()
# You can generate a Token from the "Tokens Tab" in the UI
token  = os.getenv('TOKEN')
org    = os.getenv('ORG')
bucket = os.getenv('BUCKET')
client = InfluxDBClient(url="http://localhost:8086", token=token)


# Data Write Method 1
class InfluxClient:
    def __init__(self,_token,_org,_bucket): 
        self._org    = _org 
        self._bucket = _bucket
        self._client = InfluxDBClient(url="http://localhost:8086", token =_token)
    
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
    # def query_data(self,query):
    # query_api = self._client.query_api()
    # result = query_api.query(org=self._org, query=query)
    # results = []
    # for table in result:
    #     for record in table.records:
    #         results.append((record.get_value(), record.get_field()))
    # print(results)
    # return results

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
