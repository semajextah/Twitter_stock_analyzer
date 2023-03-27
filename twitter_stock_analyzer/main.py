import PySimpleGUI as sg
from Matplotlib_services import *
from Pull_stock_data import *
from Pull_twitter_data import *
import re

#test account KTreibstoff
# to the window
sg.theme('DarkPurple6')

# Very basic window.
layout = [
    [sg.Text('Please enter the details')],
    [sg.Text('Name', size=(15, 1)), sg.InputText()],
    [sg.Text('# of Tweets', size=(15, 1)), sg.InputText()],
    [sg.Text('Time Delta', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Simple data entry window', layout)
event, values = window.read()
window.close()





tweets = scrape_tweets(values[0], int(values[1]))
stock_symbols = grab_all_symbols()

stocks_mentioned = {}

#normalizes date
tweets['date'] = tweets['date'].astype(str)
tweets['date'] = tweets['date'].str[:10]

#parses tweets for stock prices after removing special characters
#adds any values that exist within the stock symbols to a dictionary with stock symbol as the key
for index, i in tweets.iterrows():
    listed_tweets = []
    comment_as_list = list(map(str, i['content'].split(" ")))
    comment_as_list = [re.sub(r'^[^A-Za-z]+|[^A-Za-z]', '', i) for i in comment_as_list]
    for index, i2 in stock_symbols.iterrows():
        for l1 in comment_as_list:
            if i2['Stock_Symbol'] == l1:
                if i2['Stock_Symbol'] not in stocks_mentioned:
                    stocks_mentioned[i2['Stock_Symbol']] = []
                stocks_mentioned[i2['Stock_Symbol']].append(i['date'])


#checks if any values exist within the dictionary and sends them to be plotted
if any(stocks_mentioned):
    for k,v in stocks_mentioned.items():
        if isinstance(v, list):
            for d in v:
                orig, start, end = date_manipulation(d , int(values[2]))
                stock_prices = price_range_check(k, start, end)
                plot_stock(stock_prices, values[0], str(k), orig)
















