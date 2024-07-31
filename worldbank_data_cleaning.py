# -*- coding: utf-8 -*-

#import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('/content/world_bank_data_combined.xlsx')
df.head()

df.columns

#rename columns
df = df.rename(columns = {'1990 [YR1990]':'1990',
                          '2000 [YR2000]':'2000',
                          '2014 [YR2014]':'2014',
                          '2015 [YR2015]':'2015',
                          '2016 [YR2016]':'2016',
                          '2017 [YR2017]':'2017',
                          '2018 [YR2018]':'2018',
                          '2019 [YR2019]':'2019',
                          '2020 [YR2020]':'2020',
                          '2021 [YR2021]':'2021',
                          '2022 [YR2022]':'2022',
                          '2023 [YR2023]':'2023'})
df.columns

#drop columns
df = df.drop(['Series Code', '1990', '2000'], axis=1)

#remove the unnecessary content
removed_factors = [
    'Population density (people per sq. km of land area)',
    'GNI, Atlas method (current US$)',
    'GNI, PPP (current international $)',
    'GNI per capita, Atlas method (current US$)',
    'GNI per capita, PPP (current international $)',
    'Revenue, excluding grants (% of GDP)',
    'Domestic credit provided by financial sector (% of GDP)',
    'School enrollment, primary and secondary (gross), gender parity index (GPI)',
    'Fertility rate, total (births per woman)',
    'Contraceptive prevalence, any method (% of married women ages 15-49)',
    'Terrestrial and marine protected areas (% of total territorial area)',
    'Annual freshwater withdrawals, total (% of internal resources)',
    'Statistical Capacity Score (Overall Average) (scale 0 - 100)',
    'Poverty headcount ratio at national poverty lines (% of population)',
    'Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)',
    'Income share held by lowest 20%',
    'Adolescent fertility rate (births per 1,000 women ages 15-19)',
    'Births attended by skilled health staff (% of total)',
    'Prevalence of underweight, weight for age (% of children under 5)',
    'Gross capital formation (% of GDP)',
    'High-technology exports (% of manufactured exports)',
    'Merchandise trade (% of GDP)',
    'Net barter terms of trade index (2015 = 100)',
    'External debt stocks, total (DOD, current US$)',
    'Total debt service (% of exports of goods, services and primary income)',
    'Personal remittances, received (current US$)',
    'Net official development assistance and official aid received (current US$)'
]

df = df[~df['Series Name'].isin(removed_factors)].reset_index(drop=True)
df

#roundoff big decimal numbers
import numpy as np
for col in df.columns[1:]:
  df[col] = df[col].apply(lambda x: round(x, 2) if isinstance(x, (float, np.floating)) else x)

df.replace('..', pd.NA, inplace=True)

# Melt the DataFrame to transform year columns into a 'Year' column
melted_df = df.melt(
    id_vars=['Country Name', 'Country Code', 'Series Name'],
    value_vars=['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    var_name='Year',
    value_name='Value'
)

# Pivot the melted DataFrame
pivoted_df = melted_df.pivot_table(
    index=['Country Name', 'Country Code', 'Year'],
    columns='Series Name',
    values='Value',
    aggfunc='first'
).reset_index()

pivoted_df

pivoted_df.isnull().sum()

#save cleaned file
pivoted_df.to_csv('world_bank_data_cleaned.csv', index=False)
pivoted_df.to_excel('world_bank_data_cleaned.xlsx', index=False)

"""# FastAPI"""

!pip install fastapi uvicorn nest-asyncio pyngrok

import json
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
import nest_asyncio
from pyngrok import ngrok
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/world_bank_data_cleaned")
async def download_file():
    file_path = "world_bank_data_cleaned.csv"
    return FileResponse(file_path, media_type='text/csv', filename='world_bank_data_cleaned.csv')

@app.get("/country/{country_name}")
async def get_country_data(country_name: str):
    df = pd.read_csv("world_bank_data_cleaned.csv")
    country_data = df[df['Country Name'] == country_name]

    if country_data.empty:
        return {"error": "Country not found"}
    else:
        # Convert the DataFrame to an HTML table
        html_table = country_data.to_html(index=False)
        return HTMLResponse(content=html_table, status_code=200)

# Replace the following line with your actual ngrok authtoken
# !ngrok authtoken YOUR_NGROK_AUTHTOKEN

ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
File_url = ngrok_tunnel.public_url + '/world_bank_data_cleaned'
print(File_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)

