#Connecting to postgres db
from sqlalchemy import create_engine, text
import pandas as pd

#Defining the connection details
username = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5432'
database = '10ACADEMY_TELECOM'

# Database connection 
connection = f'postgresql://{username}:{password}@{host}:{port}/{database}'

#DB Engine creation
db_engine = create_engine(connection)

#establishing a connection
conn = db_engine.connect()
print('connected sucessfully')

#sql query
query = text('SELECT * FROM xdr_data')

result = conn.execute(query)
print(result)
print('*' * 50)

#changing the data to a dataframe
df = pd.read_sql_query(query, conn )
print(df.head())

#changing the dataframe to csv file and downloading it
df.to_csv('telecom.csv', index= False)
