import json
import numpy as np
import pandas
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

city_average = '''CREATE TABLE city_average_tugmenau(
                    city int,
                    average_salary int,
                    Number_of_players int
                )'''

mycursor.execute(city_average)


zxc = mycursor.execute("SELECT * FROM nba_players", params=None)
rows = mycursor.fetchall()
df_player = pd.DataFrame(rows)

zxc = mycursor.execute("SELECT * FROM nba_salary", params=None)
rows = mycursor.fetchall()
df_salary = pd.DataFrame(rows)

zxc = mycursor.execute("SELECT * FROM nba_savings", params=None)
rows = mycursor.fetchall()
df_savings = pd.DataFrame(rows)

col1 = new_df.groupby(9).count()[10].reset_index(name='num')
new_df = new_df.groupby(10).mean()['1_x'].reset_index(name='average_salary')
new_df['Number_of_players'] = col1['num']
new_df.rename(columns={10 : 'city'}, inplace=True)
