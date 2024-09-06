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


# ------ Data Transformation & Enrichment ------ #

# convert 'updated' column into actual date-time format
df_cleaned['updated'] = pd.to_datetime(df_cleaned['updated'], unit='ms')
print('updated column: ', df_cleaned['updated'])

# Add new column: Case Fatility Rate (CFR) = (Deaths / Cases) * 100
df_cleaned['Case Fatility Rate'] = (df_cleaned['deaths'] / df_cleaned['cases']) * 100
print('Case Fatility Rate: ', df_cleaned['Case Fatility Rate'])



