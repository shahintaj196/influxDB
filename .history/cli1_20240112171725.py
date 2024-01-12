import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token  = 'HTAAR9B4CYXPZmEPlHQDDyjmMJ-5xDTl9Tcln-7Nrak6zDezqJ3YIU_XYnZ9NBPRlCFWPbLUmPYXGlO5TLoMRg=='
org = "agah"
url = "http://localhost:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket="tse"

write_api = client.write_api(write_options=SYNCHRONOUS)
   
for value in range(5):
    point = (
        Point("measurement1")
        .tag("tagname1", "tagvalue1")
        .field("field1", value)
    )
    write_api.write(bucket=bucket, org="agah", record=point)
    time.sleep(1) # separate points by 1 second
    
query_api = client.query_api()

query = """from(bucket: "tse")
    |> range(start: -10m)
    |> filter(fn: (r) => r._measurement == "measurement1")"""
    tables = query_api.query(query, org="agah")

for table in tables:
    for record in table.records:
        print(record)
query_api = client.query_api()

query = """from(bucket: "tse")
  |> range(start: -10m)
  |> filter(fn: (r) => r._measurement == "measurement1")
  |> mean()"""
tables = query_api.query(query, org="agah")

for table in tables:
    for record in table.records:
        print(record)
