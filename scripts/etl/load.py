import pandas as pd
import psycopg2 as psy

# Import pre-processed raw dataset
df = pd.read_csv('data/processed/east_africa_covid_data_transformed.csv')

# Connect to PostgreSQL
conn = psy.connect(
    host='localhost', database='covid19_project', user='postgres', passwd='Developer'
)

cursor = conn.cursor()