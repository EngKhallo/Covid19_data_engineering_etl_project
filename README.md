<h1 align="center">COVID-19 Data Engineering Pipeline</h1>

This project is a complete end-to-end data engineering pipeline that extracts, transforms, and loads (ETL) COVID-19 data for East African countries. The pipeline is built using Python, PostgreSQL, and Apache Airflow for automation. It includes data cleaning, transformation, and analytics-ready storage, with capabilities for scheduling and automation.

<h2>Features</h2>
- **Data Extraction**: Pulls live COVID-19 data for 12 East African countries from the disease.sh API.
- **Data Transformation**: Cleans and transforms raw data by:
  - Handling missing values and duplicates.
  - Creating new features like Case Fatality Rate (CFR) and Recovery Rate.
  - Converting timestamps into readable date formats.
- **Data Loading**: Stores data into a PostgreSQL database with separate countries and metrics tables.
- **Workflow Automation**: Automates the ETL process using scheduler.py and supports Apache Airflow for more advanced workflows.
- **Data Analysis**: Provides SQL scripts for performing analysis and creating visualizations.

<h2>Project Structure</h2>
COVID19_PROJECT/
├── data/
│   ├── raw/                     # Raw datasets (CSV)
│   ├── processed/               # Transformed datasets (CSV)
│   ├── warehouse/               # Data warehouse storage files (if needed)
├── scripts/
│   ├── etl/
│   │   ├── extract.py           # Extracts data from the API
│   │   ├── transform.py         # Cleans and transforms the raw data
│   │   ├── load.py              # Loads the transformed data into PostgreSQL
│   ├── analysis/
│   │   ├── create_tables.sql    # SQL script to create PostgreSQL tables
│   │   ├── data_analysis.sql    # SQL scripts for data analysis
│   ├── automation/
│   │   ├── scheduler.py         # Schedules the ETL process
├── src/
│   ├── img/                     # Images for documentation
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation

