# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 22:00:06 2020

@author: ANURAG
"""




# import needed libraries
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Make function for calls to Yahoo Finance
def get_adj_close(ticker, start, end):
    '''
    A function that takes ticker symbols, starting period, ending period
    as arguments and returns with a Pandas DataFrame of the Adjusted Close Prices
    for the tickers from Yahoo Finance
    '''
    start = start
    end = end
    info = web.DataReader(ticker, data_source='yahoo', start=start, end=end)['Adj Close']
    return pd.DataFrame(info)

# Get Adjusted Closing Prices for Facebook, Tesla and Amazon between 2018-2020
fb = get_adj_close('ambujacem.ns', '1/2/2018', '9/10/2020')
#fb = get_adj_close('fb', '1/2/2016', '31/12/2017')
tesla = get_adj_close('tsla', '1/2/2018', '9/10/2020')
amazon = get_adj_close('amzn', '1/2/2018', '9/10/2020')

#Changing the price to inr
#fb["Adj Close"] = 73 * fb['Adj Close']   

# Calculate 30 Day Moving Average, Std Deviation, Upper Band and Lower Band
for item in (fb,tesla):
    item['30 Day MA'] =( item['Adj Close'].rolling(window=20).mean())
    
    # set .std(ddof=0) for population std instead of sample
    item['30 Day STD'] =( item['Adj Close'].rolling(window=20).std()) 
    
    item['Upper Band'] = (item['30 Day MA'] + (item['30 Day STD'] * 2))
    item['Lower Band'] =( item['30 Day MA'] - (item['30 Day STD'] * 2))



# Simple 30 Day Bollinger Band 
fb[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))

plt.title('30 Day Bollinger Band')
plt.ylabel('Price (Rs)')
plt.show();


# set style, empty figure and axes
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)

# Get index values for the X axis for facebook DataFrame
x_axis = fb.index.get_level_values(0)

# Plot shaded 21 Day Bollinger Band for Facebook
ax.fill_between(x_axis, fb['Upper Band'], fb['Lower Band'], color='grey')

# Plot Adjust Closing Price and Moving Averages
ax.plot(x_axis, fb['Adj Close'], color='blue', lw=2)
ax.plot(x_axis, fb['30 Day MA'], color='black', lw=2)

# Set Title & Show the Image
ax.set_title('30 Day Bollinger Band For Infosys')
ax.set_xlabel('Date (Year/Month)')
ax.set_ylabel('Price(Rs)')
ax.legend()
plt.show()
