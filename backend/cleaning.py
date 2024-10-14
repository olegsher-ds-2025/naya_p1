import pandas as pd
import sys
import logging

from api import work_with_frames


logging.basicConfig(level=logging.DEBUG)
pd.set_option('display.max_columns', 43)

logging.info('Linux kernel is ' + sys.version)
logging.info('Pandas version is ' + pd.__version__)

df = work_with_frames()
logging.info(type(df))
# logging.info(f'Shape: {df.shape}')
# logging.info(f'Describe: {df.describe()}')
logging.info(f'INfo: {df.info(max_cols=50)}')
logging.info(df.head())
logging.info(df.tail())
logging.info(df.sample(5))
logging.info(df.columns)
logging.info(df.index)
logging.info(df['USD'].min())
logging.info(df[df.columns[:-1:]])
logging.info(df.select_dtypes(object))
# logging.info('\n',str(df.iloc[:10,:9]))
print('\n',df.iloc[[5]])
print('\n',df.loc[:10,['Date','USD','BRL']])
print('\n',df.loc[~((df['Date'] == '2024-10-04') | (df['Date'] == '2024-09-25')),['Date','USD','BRL']])

print('\n', df.query('Date > "2024-10-04"'))
print(df['USD'].count())

print(df[['USD', 'ILS', 'GBP']].agg(['mean', 'min', 'max']))
print('rolling \n')
print(df[['USD']].rolling(window=5).max())

