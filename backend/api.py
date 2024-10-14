import requests, zipfile, io
import pandas as pd
import datetime

SINGLE_DAY_ECB = 'eurofxref.csv'
ECB = 'eurofxref-hist.csv'

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
        # fetch_csv()


def work_with_frames():
   return pd.read_csv(ECB)


def work_with_series():
    return pd.read_csv(SINGLE_DAY_ECB, header=0).squeeze()

def get_current_data_day():
    return ds_single_day['Date']


if '__init__' == '__main__':

    ds_single_day = work_with_series()
    date = ds_single_day['Date'][0]
    refresh_data(date)


    ds_single_day = work_with_series()
    df_ecb = work_with_frames()
    # print(df_ecb.head())
    # print(df_ecb.info())
    # df_ecb.set_index('hello', inplace=True)
    # print(df_ecb)
    # print(ds_single_day.set_index('Test'))
    # Cleaning data
    data_single_day = ds_single_day.replace(' ', None).replace(ds_single_day['Date'], None).dropna().to_dict()
    current_data_day = ds_single_day['Date']
    # print(data_single_day.set_index('Test'))


