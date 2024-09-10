CREATE TABLE countries (
    country_id SERIAL PRIMARY KEY,  -- Auto-incrementing unique ID for each country
    country_name VARCHAR(100),      -- Country name (e.g., "Somalia")
    iso2 CHAR(2),                   -- 2-letter country code (e.g., "SO")
    iso3 CHAR(3),                   -- 3-letter country code (e.g., "SOM")
    lat FLOAT,                      -- Latitude (e.g., 10.0)
    long FLOAT                      -- Longitude (e.g., 49.0)
);

CREATE TABLE metrics (
    metric_id SERIAL PRIMARY KEY,        -- Unique metric entry ID
    country_id INT REFERENCES countries(country_id), -- Foreign key to countries table
    updated DATE,                        -- Date of the metric
    total_cases INT,                     -- Total COVID-19 cases
    today_cases INT,                     -- Cases reported today
    total_deaths INT,                    -- Total COVID-19 deaths
    today_deaths INT,                    -- Deaths reported today
    recovered INT,                       -- Total recovered cases
    today_recovered INT,                 -- Recovered cases reported today
    active INT,                          -- Currently active cases
    critical INT,                        -- Number of critical cases
    cases_per_million FLOAT,             -- Total cases per million people
    deaths_per_million FLOAT,            -- Total deaths per million people
    recovered_per_million FLOAT,         -- Total recovered per million people
    critical_per_million FLOAT,          -- Critical cases per million people
    case_fatality_rate FLOAT,            -- Case Fatality Rate
    recovered_rate FLOAT                 -- Recovered rate
);



