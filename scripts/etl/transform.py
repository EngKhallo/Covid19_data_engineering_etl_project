import pandas as pd

# Import pre-processed raw dataset
df = pd.read_csv('data/raw/east_africa_covid_data.csv')

# Check for missing values
print(df.isnull().sum())
# output: every thing is 0

# Drop rows with missing values and place it in a new variable if exist
df_cleaned = df.dropna()

# Duplicates
print(df.duplicated().sum())
# output: every thing is 0



