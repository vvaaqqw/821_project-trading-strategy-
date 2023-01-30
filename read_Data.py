#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 14:04:11 2023

@author: wys
"""
import numpy as np
import pandas as pd

import yfinance as yf

import datetime
import requests
import bs4 as bs


#get S&P tickers list from wikipedia
resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = bs.BeautifulSoup(resp.text, 'lxml')
table = soup.find('table', {'class': 'wikitable sortable'})

tickers = []

for row in table.findAll('tr')[1:]:
    ticker_name = row.findAll('td')[0].text
    tickers.append(ticker_name)

#clean list
tickers = [s.replace('\n', '') for s in tickers]

#get data from yfin
start = datetime.datetime(2020, 1, 1)
end = datetime.datetime(2022, 6, 1)
data = yf.download(tickers, start=start, end=end)
'''
#clean data
df = data.stack().reset_index().rename(index=str, columns={"level_1": "Symbol"}).sort_values(['Symbol','Date'])
df.set_index('Date', inplace=True)
'''

print(data)