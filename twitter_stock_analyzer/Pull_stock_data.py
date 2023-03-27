import datetime

import pandas as pd
import yfinance as yf
from yahoo_fin import stock_info as si

yf.pdr_override()


#class Stocks:
def grab_all_symbols():
    # gather stock symbols from major US exchanges
    df1 = pd.DataFrame( si.tickers_sp500() )
    df2 = pd.DataFrame( si.tickers_nasdaq() )
    df3 = pd.DataFrame( si.tickers_dow() )
    df4 = pd.DataFrame( si.tickers_other() )

    # convert DataFrame to list, then to sets
    sym1 = set( symbol for symbol in df1[0].values.tolist() )
    sym2 = set( symbol for symbol in df2[0].values.tolist() )
    sym3 = set( symbol for symbol in df3[0].values.tolist() )
    sym4 = set( symbol for symbol in df4[0].values.tolist() )

    # join the 4 sets into one. Because it's a set, there will be no duplicate symbols
    symbols = set.union( sym1, sym2, sym3, sym4 )

    # Some stocks are 5 characters. Those stocks with the suffixes listed below are not of interest.
    my_list = ['W', 'R', 'P', 'Q']
    del_set = set()
    sav_set = set()

    for symbol in symbols:
        if len( symbol ) > 4 and symbol[-1] in my_list:
            del_set.add( symbol )
        else:
            sav_set.add( symbol )

    stock_symbols = pd.DataFrame (symbols, columns = ['Stock_Symbol'])
    return stock_symbols
    


def price_range_check(symbol, start, end):
    data = yf.download(symbol, start, end)
    return data


def date_manipulation(listed_date, delta: int):
    tweet_date = pd.to_datetime(listed_date)
    start = tweet_date + datetime.timedelta(days = -delta)
    end = tweet_date + datetime.timedelta(days = delta)
    tweet_date = tweet_date.strftime('%Y-%m-%d')
    start =start.strftime('%Y-%m-%d')
    end = end.strftime('%Y-%m-%d')
    return tweet_date, start, end