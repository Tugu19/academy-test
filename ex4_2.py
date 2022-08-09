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

city_average = '''CREATE TABLE players_average_tugmenau(
                    full_name varchar(25),
                    above_average_salary int
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

avg = df_salary.mean()[1]
new_df = df_player[2].reset_index(name='full_name')
new_df['last'] = df_player[5]
new_df['full_name'] = new_df['full_name'] + ' ' + new_df['last']
new_df = new_df.drop(columns=['last'])
df_salary.rename(columns={0 : 'index'}, inplace=True)
new_df = pd.merge(new_df, df_salary, on='index', how='inner')
new_df['above_average_salary'] = np.where(df_salary[1] > avg, 1, 0)
