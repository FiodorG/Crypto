import pandas as pd
import numpy as np

def import_data():
    df = pd.read_csv("../data/close.csv", index_col=0, parse_dates=True)
    df.drop(["ETH-BTC", "BTC-EUR"], axis=1, inplace=True)

    # Hopefully these are data errors and not crazy real prints
    df.loc["2017-06", "DOGE"] = np.nan
    df.loc["2017-09-01", "FUN"] = np.nan
    df.loc[:"2018-03", "XLM"] = np.nan
    df.loc[:"2017-12-08", "BCH"] = np.nan
    df.loc["2017-06-12": "2017-06-15", "ETC"] = np.nan
    df.loc["2018-11-11":"2018-11-21", "BCH"] = np.nan
    df.loc["2019-06-03":"2019-06-10", "KNC"] = np.nan
    
    return df