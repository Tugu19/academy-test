 import json
 import pandas as pd
 import requests
 import mysql.connector
 from sqlalchemy import create_engine

 mydb = mysql.connector.connect(
   host="34.163.182.248",
   port=3306,
   user="root",
   password="Ciocanul12@",
   database="academy"
 )

 mycursor = mydb.cursor()

 response = requests.get('https://www.balldontlie.io/api/v1/players')
 data = response.text
 data = json.loads(data)
 print(data)

 data100 = []
 for i in range(1, 101):
     response1 = requests.get(f'https://www.balldontlie.io/api/v1/players/{i}')
     datanew = response1.text
     data100.append(datanew)
     print(datanew)
