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

# Insert metrics into the 'metrics' table
for index, row in df.iterrows():
    cursor.execute("SELECT country_id FROM countries WHERE country_name = %s", (row['country'],))
    country_id = cursor.fetchone()[0]
    
    cursor.execute("""
        INSERT INTO metrics (country_id, updated, total_cases, today_cases, total_deaths, today_deaths, recovered, today_recovered, 
                             active, critical, cases_per_million, deaths_per_million, recovered_per_million, critical_per_million, 
                             case_fatality_rate, recovered_rate)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        country_id, row['updated'], row['total_cases'], row['todayCases'], row['total_deaths'], row['todayDeaths'],
        row['recovered'], row['todayRecovered'], row['active'], row['critical'], row['casesPerOneMillion'], 
        row['deathsPerOneMillion'], row['recoveredPerOneMillion'], row['criticalPerOneMillion'],
        row['case_fatility_rate'], row['recovered_rate']  # Update here
    ))

# Commit changes to the 'metrics' table
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
