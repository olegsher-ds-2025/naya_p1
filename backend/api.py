import requests, zipfile, io
import pandas as pd

ECB_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip"
SINGLE_DAY_ECB_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip"

ECB = 'eurofxref.csv'
SINGLE_DAY_ECB = 'eurofxref-hist.csv'

# r = requests.get(ECB_URL)
# z = zipfile.ZipFile(io.BytesIO(r.content))
# z.extractall(".")

# r = requests.get(SINGLE_DAY_ECB_URL)
# z = zipfile.ZipFile(io.BytesIO(r.content))
# z.extractall(".")

df_single_day = pd.read_csv(SINGLE_DAY_ECB)
df_single_day.info()
print(df_single_day)


df_ecb = pd.read_csv(ECB)
df_ecb.info()
print(df_ecb, df_ecb.describe())

x = df_ecb.to_html()
y = df_ecb.to_json()






# from currency_converter import CurrencyConverter
# c = CurrencyConverter()
# # c.convert(100, 'EUR', 'USD')
# # print(c.convert(100, 'EUR', 'USD'))

# with open(c.SINGLE_DAY_CURRENCY_FILE) as f:
#     s = f.read()


# print(s)