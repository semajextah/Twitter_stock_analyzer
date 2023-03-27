
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
from Pull_stock_data import *
from Pull_twitter_data import *


def plot_stock(stock_plot, user_name, stock_sym, start):
    plt.axvline(pd.Timestamp(start),color='r')
    stock_plot['Open'].plot(figsize = (15,7))
    plt.title('Twitter User : ' + str(user_name) + " | Stock Symbol - " + stock_sym)
    plt.show()
    pass


def save_multi_image(filename):
    pp = PdfPages(filename)
    fig_nums = plt.get_fignums()
    figs = [plt.figure(n) for n in fig_nums]
    for fig in figs:
        fig.savefig(pp, format='pdf')
    pp.close()