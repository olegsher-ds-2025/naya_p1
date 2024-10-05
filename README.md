
# First project,  Naya course.

## Fetch file from internet using requests package and load to pandas

The code [api.py](backend/api.py) fetch latest foregn currency dataset(csv)     
from `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip` and from 
`https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip` load it to pandas and export results to Flask based web application and Telegram bot

```
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
```


## Simple Telegram bot

Telegram bot screenshot:
![Telegram bot screenshot.](images/telegram.png)


Handle messages in bot:
```
def handle_message(update, context) -> None:
    user_message = update.message.text
    if user_message == 'GBP':
        update.message.reply_text(f'GBP/EUR {z.get(" GBP")[0]}')
    elif user_message == 'USD':
        update.message.reply_text(f'USD/EUR {z.get(" USD")[0]}')
    elif user_message == 'ILS':
        update.message.reply_text(f'ILS/EUR {z.get(" ILS")[0]}')
    else:
        update.message.reply_text(f'You said: {user_message}')
```


## Flask web server

Flask app available on
[http://naya_p1.sher.biz/rates](http://naya_p1.sher.biz/rates)
code:

```
@app.route('/')
def home():
    return render_template('index.html', x=x, y=y)

@app.route('/rates')
def rates():
    return render_template('my_file.html', 
                           z = z.get('Date'), 
                           usd = z.get(' USD'), 
                           gbp = z.get(' GBP'), 
                           ils = z.get(' ILS')
                           )
```
HTML (Jinja) file: 
```
{{ z[0] }}
<br/>USD/EUR - {{ usd[0] }}
<br/>GBP/EUR - {{ gbp[0] }}
<br/>ILS/EUR - {{ ils[0] }}
```


![](images/Screenshot%20from%202024-10-05%2022-51-07.png)




