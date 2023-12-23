# -*- coding: utf-8 -*-
"""Historical_VaR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TnPPeELggUHcUk4V4UwlPNUGJ4hYml9T

# **Value at Risk**

---

Import Necessary Libraries
"""

import numpy as np
import pandas as pd
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import norm

"""Set Time to a certain number of years"""

years = 5
endDate= dt.datetime(2023,10,16)
startDate = endDate - dt.timedelta(days=365*years)

"""Creating a list of Indexes"""

tickers = ['^NSEI','^BSESN']

"""Download daily adjusted closing prices for the Indices"""

adj_close_df = pd.DataFrame()
for i in tickers:
  data=yf.download(i, start=startDate, end=endDate)
  adj_close_df[i]=data['Adj Close']
print (adj_close_df)


"""Calculate the simple daily returns and drop any NAs"""

daily_returns = adj_close_df / adj_close_df.shift(1) - 1
daily_returns = daily_returns.dropna()
print(daily_returns)

"""Create a portfolio"""

weights=np.array([1/len(tickers)]*len(tickers))
print(weights)

"""Calculate the historical portfolio returns"""

historical_returns=(daily_returns*weights).sum(axis=1)
historical_returns_df = historical_returns.to_frame()
historical_returns_df.columns = ['Portfolio returns']
print(historical_returns_df)

"""Find X day historical returns"""

days = 1
range_returns = historical_returns_df.rolling(window=days).sum()
range_returns = range_returns.dropna()
print(range_returns)

"""Specify a Confidence interval and calculate the Value at Risk (VaR) using historical method"""

confidence_interval=0.99
VaR= np.percentile(range_returns, 100-(confidence_interval*100))
VaR_percent=VaR*100
print(f'{VaR_percent:.2f}%')

"""Plot the results of the historical returns"""

return_window=days
range_returns = historical_returns_df.rolling(window=return_window).sum()
range_returns = range_returns.dropna()
plt.hist(range_returns*100, bins=50, density=True)  # Multiply by 100 to convert to percentage
plt.xlabel(f'{return_window}- Day Portfolio Return (Percentage value)')
plt.ylabel('Frequency')
plt.title(f'Distribution of Portfolio {return_window}-Day Returns (Percentage value)')
VaR_percent = VaR * 100  # Convert VaR to percentage
plt.axvline(VaR_percent, color='r', linestyle='dashed', linewidth=2, label=f'VaR at {confidence_interval:.0%} confidence level: {VaR_percent:.2f}%')  # Show VaR value on the line
plt.legend()
plt.show()