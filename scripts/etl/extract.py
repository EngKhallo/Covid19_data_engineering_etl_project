import requests
import pandas as pd

def extract_data():
    # URL for all 13 east african countries
    url = "https://disease.sh/v3/covid-19/countries/Burundi%2C%20Comoros%2C%20Djibouti%2C%20Ethiopia%2C%20Eritrea%2C%20Kenya%2C%20Rwanda%2C%20Seychelles%2C%20Somalia%2C%20South%20Sudan%2C%20Sudan%2C%20Tanzania%2C%20and%20Uganda%20%20"

    response = requests.get(url)
    data = response.json()

    # Convert JSON to DataFrame
    df = pd.json_normalize(data)

    # save to csv format
    df.to_csv('data/raw/east_africa_covid_data.csv', index=False)
