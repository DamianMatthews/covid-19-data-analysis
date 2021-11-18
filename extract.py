import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3 as sl
import requests
import json
import pandas as pd

# connecting to database
con = sl.connect('my-test.db')

# extracting data from API
response_API = requests.get('https://api.covidtracking.com/v1/states/daily.json')
data = response_API.text
parse_json = json.loads(data)

# changing data from json format to a dataframe 
covid_data = pd.json_normalize(parse_json)

# creating dataframes to load 3 sql tables we created
df_covid_hospitalizations = covid_data[['date', 'state','hospitalized','hospitalizedCurrently','hospitalizedCumulative']]
df_covid_deaths = covid_data[['date', 'state','death']]
df_covid_tests = covid_data[['date','state','negative','totalTestResults']]

df_covid_hospitalizations.to_sql('covid_hospitalization_table', con, if_exists='append', index=False)
df_covid_deaths.to_sql('covid_deaths_table', con, if_exists='append', index=False)
df_covid_tests.to_sql('covid_tests_table', con, if_exists='append', index=False)