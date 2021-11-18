# this is our main file 
import matplotlib as mpl
import extract
import seaborn as sns
import sqlite3 as sl
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import transform

sns.set_theme(style="ticks")

sns.set_theme(style="whitegrid")

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 30))

# Plot the total hospitalizations for 2020
sns.set_color_codes("pastel")
sns.barplot(x="hospitalized", y="state", data=extract.df_pivoted_hospilizations,
            label="Total hospitalizations", color="b", ci=None)

# Plot the total deaths by state for 2020
sns.set_color_codes("muted")
sns.barplot(x="death", y="state", data=extract.df_pivoted_deaths,
            label="Total Deaths by State", color="b", ci=None)

# Add a legend and informative axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(ylabel="",
       xlabel="This data covers the year 2020")
sns.despine(left=True, bottom=True)

plt.show()