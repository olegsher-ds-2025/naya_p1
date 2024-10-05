import requests, zipfile, io
import pandas as pd
import datetime

ECB = 'eurofxref.csv'
SINGLE_DAY_ECB = 'eurofxref-hist.csv'

today: str =  str(datetime.datetime.today())[:10]

def fetch_csv() -> None:
    ECB_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip"
    SINGLE_DAY_ECB_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip"
    r = requests.get(ECB_URL)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(".")

    r = requests.get(SINGLE_DAY_ECB_URL)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(".")

def refresh_data(date) -> None:
    print(f'Today is {today} and file from {date}')
    if today is not date: # TODO BUG refactor to get date from remote file
        print('fetching new data...')
        fetch_csv()



df_single_day = pd.read_csv(SINGLE_DAY_ECB)
date = df_single_day['Date'][0]
refresh_data(date)

df_single_day = pd.read_csv(SINGLE_DAY_ECB)
df_ecb = pd.read_csv(ECB)


x = df_ecb.to_html()
y = df_ecb.to_json()
z = df_ecb.to_dict()
