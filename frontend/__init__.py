from flask import Flask, redirect, url_for, request, render_template
# from backend.api import x,y



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

df_ecb.to_html(open('frontend/templates/my_file.html', 'w'))
y = df_ecb.to_json()
z = df_ecb.to_dict()

for key, value in z.items():
    print(key, value)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', x=z, y=y)


@app.route('/rates')
def rates():
    return render_template('my_file.html')
