import pandas as pd
from pandas import DataFrame,Series
import numpy as np
import datetime
import pandas.io.data as web
import quandl

# a = web.DataReader("GBP=X", 'yahoo')
# a = web.DataReader("JPY=X", 'yahoo')
# jpy = web.get_data_fred('DEXJPUS')
# print jpy

def get_data():
    data = quandl.get("ECB/EURUSD", authtoken="G-_-G7yn75tX64T3fKXc")
    print data.head()

def main():
    print "s"

if __name__ == "__main__":
    main()
    data = get_data()
