import pandas as pd
import sqlalchemy as db
import requests
import json


API_KEY = "AIzaSyAYP2C_aLg1ll-oYvwwdgaYjAJJVGNNMDM "

url = 'https://developers.google.com/youtube/v3/'
response = requests.post(url)
print(response)

df = pd.DataFrame.from_dict()
print(df)

engine = db.create_engine('')

df.to_sql('', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
   print(pd.DataFrame(query_result))
