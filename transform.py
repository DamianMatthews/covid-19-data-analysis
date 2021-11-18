import extract
import seaborn as sns
import sqlite3 as sl
import requests
import json
import pandas as pd

# connecting to database
con = sl.connect('my-test.db')

# use SQL to create pivoted data and return to dataframe for visualizing
extract.df_pivoted_deaths = pd.read_sql('select sum(death) as death, state, date \
from (select sum(death) as death, state, substr(date,1,4) as date from covid_deaths_table \
group by state, substr(date,1,6)) where date ="2020" \
group by state, date order by 1 desc', con)

# use SQL to create pivoted data and return to dataframe for visualizing
extract.df_pivoted_hospilizations = pd.read_sql('select sum(hospitalized) as hospitalized, state, date \
from (select sum(hospitalized) as hospitalized, state, substr(date,1,4) as date from covid_hospitalization_table \
group by state, substr(date,1,6)) where date ="2020" \
group by state, date order by 1 desc', con)

# use SQL to create pivoted data and return to dataframe for visualizing
extract.df_pivoted_tests = pd.read_sql('select sum(totalTestResults) as totalTestResults, state, date \
from (select sum(totalTestResults) as totalTestResults, state, substr(date,1,4) as date from covid_tests_table \
group by state, substr(date,1,6)) where date ="2020" \
group by state, date order by 1 desc', con)
