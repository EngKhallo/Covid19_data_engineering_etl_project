import schedule
import time
from extract import extract_data
from transform import transform_data
from load import load_data

def etl_job():
   # Extract the raw data
    extract_data()
    # Transform the data
    transform_data()  # Remove the argument here
    # Load the data into the database
    load_data()

# Schedule the job to run daily
schedule.every().day.at("17:04").do(etl_job)

while True:
    schedule.run_pending()
    time.sleep(1)
