from io import BytesIO
from azure.storage.blob import BlobServiceClient
import pandas as pd


df1 = pd.read_csv("salary_download.csv")
df1.rename(columns={'Unnamed: 0' : 'Index'}, inplace=True)

df2 = pd.read_csv("savings_download.csv")
df2.rename(columns={'Unnamed: 0' : 'Index'}, inplace=True)

df = pd.merge(df1, df2, on='Index', how='inner').set_index('Index')
df.to_csv("Andrei_Tugmeanu.csv")

