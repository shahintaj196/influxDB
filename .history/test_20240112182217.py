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

#!-------------+
#!    Write    |
#!-------------+
#IC.write_data(["MSFT,stock=MSFT Open=62.79,High=63.84,Low=62.13"])



# MSFT_file = open('FINANCE.csv')
# csvreader = csv.reader(MSFT_file)
# header = next(csvreader)
# rows = []

# IC.query_data(query1)
# for row in csvreader:
#         date,open,high,low = row[0],row[1],row[2],row[3]
#         line_protocol_string = ''
#         line_protocol_string+=f'MSFT_{date},'
#         line_protocol_string+=f'stock=MSFT '
#         line_protocol_string+=f'Open={open},High={high},Low={low} '
#         line_protocol_string+=str(int(datetime.strptime(date,'%Y-%m-%d').timestamp()))
#         rows.append(line_protocol_string)
# IC.write_data(rows)
#!-------------+
#!     Read    |
#!-------------+
# query1 = 'from(bucket: "tse")\
# |> range(start: 1633124983)\
# |> filter(fn: (r) => r._field == "High")\
# |> filter(fn: (r) => r.stock == "MSFT")'

IC.delete_data("MSFT_2021-10-29")