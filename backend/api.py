import requests, zipfile, io
import pandas as pd
import datetime

SINGLE_DAY_ECB = 'eurofxref.csv'
ECB = 'eurofxref-hist.csv'

today: str =  str(datetime.datetime.today())[:10]
print(today)

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
   x = pd.read_csv(ECB)
#    print("ECB: ",type(x))
   return x 




def work_with_series():
    '''
        The function return Series object, date of object and dictionary
    '''
    
    ds = pd.read_csv(SINGLE_DAY_ECB, header=0).squeeze()
    ds_to_dict = ds.replace(' ', None).replace(ds['Date'], None).dropna().to_dict()
    modified_dictionary = {}
    for key, value in ds_to_dict.items():
        new_key = key.replace(" ", "")  #removing space between keys
        modified_dictionary[new_key] = value
    return ds, ds['Date'], modified_dictionary


if '__name__' == '__main__':

    ds_single_day = work_with_series()[0]
    print(ds_single_day)
    date = work_with_series()[1]
    print(date)
    refresh_data(date)


    ds_single_day = work_with_series()[0]
    df_ecb = work_with_frames()
    # print(df_ecb.head())
    # print(df_ecb.info())
    # df_ecb.set_index('hello', inplace=True)
    # print(df_ecb)
    # print(ds_single_day.set_index('Test'))
    # Cleaning data
    data_single_day = work_with_series()[2]
    current_data_day = ds_single_day['Date']
    # print(data_single_day.set_index('Test'))


