import pandas as pd

def transform_data():

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
    df_cleaned['updated'] = df_cleaned['updated'].dt.date  # Convert to date only
    print('updated column: ', df_cleaned['updated'])

    # Add new column: Case Fatility Rate (CFR) = (Deaths / Cases) * 100
    df_cleaned['case_fatility_rate'] = (df_cleaned['deaths'] / df_cleaned['cases']) * 100
    print('case_fatility_rate: ', df_cleaned['case_fatility_rate'])

    # Add new column: Recovered Rate but check if it exists first
    if 'recovered' in df_cleaned.columns:
        df_cleaned['recovered_rate'] = (df_cleaned['recovered'] / df_cleaned['cases']) * 100
        print('recovered_rate: ', df_cleaned['recovered_rate'])

    # Rename columns for clarity 
    df_cleaned.rename(columns={
        'cases': 'total_cases',
        'deaths': 'total_deaths', 
        'population': 'total_population'
    }, inplace=True)


    # ------ Save the cleaned and transformed data as dataset and export it ------ #
    df_cleaned.to_csv('data/processed/east_africa_covid_data_transformed.csv', index=False)

    print("Transformation complete. Processed data saved to 'data/processed/east_africa_covid_data_transformed.csv'.")






