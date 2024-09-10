import pandas as pd
import psycopg2 as psy

# Import pre-processed raw dataset
df = pd.read_csv('data/processed/east_africa_covid_data_transformed.csv')

# Connect to PostgreSQL
conn = psy.connect(
    host='localhost', database='covid19_data_pipeline', user='postgres', password='Developer'
)

cursor = conn.cursor()

# Insert Countries into the countries table
for index, row in df[['country', 'countryInfo.iso2', 'countryInfo.iso3', 'countryInfo.lat', 'countryInfo.long', 'total_population']].drop_duplicates().iterrows():
    cursor.execute("""
        INSERT INTO countries (country_name, iso2, iso3, lat, long, total_population)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (country_name) DO NOTHING;
    """, (row['country'], row['countryInfo.iso2'], row['countryInfo.iso3'], row['countryInfo.lat'], row['countryInfo.long'], row['total_population']))

# Commit changes to the 'countries' table
conn.commit()