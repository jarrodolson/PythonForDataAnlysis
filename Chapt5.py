##Basics from chapter 3
import numpy as np
from pandas import DataFrame, Series
import pandas as pd
import pandas.io.data as web

##data = {'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
##         'year':[2000,2001,2002,2001,2002],
##         'pop':[1.5,1.7,3.6,2.4,2.9]}
##frame = DataFrame(data)
##print(frame)

all_data = {}
for ticker in ['AAPL','IBM','MSFT','GOOG']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000','1/1/2010')

price = DataFrame({tic:data['Adj Close'] for tic, data in all_data.iteritems()})
volume = DataFrame({tic: data['Volume'] for tic, data in all_data.iteritems()})

returns = price.pct_change()

##Correlation for MSFT returns vs. Google returns
returns.MSFT.corr(returns.GOOG)

##Correlation matrix
returns.corr()
