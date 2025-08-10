import yfinance as yf
import numpy as np
import pandas as pd
import os
from scipy import stats
import math
from statistics import mean

from inputs import portfolio_input, num_stocks_input
from yfinance_data import base_dataframe

base_dir = os.path.dirname(__file__) 

def get_sp500_constituents():
    file_path = os.path.join(base_dir, '..', 'data', 'sp_500_stocks.csv')
    stocks = pd.read_csv(file_path)
    return stocks

def clean_dataframe(df):
    print('cleaning dataframe')
    # imputing with median/mean can create false data especially for stock data
    # hence i think this is better
    df = df.dropna()

    #-ve PBRatio usually means an accounting discrepancy or financial trouble, hence its better to filter them out just to be safe
    if 'Price to Book Ratio' in df.columns:
        df = df[df["Price to Book Ratio"] >= 0]
    return df

def calculate_percentiles(df):
    print('calculating percentiles..')
    metrics = {
        'Price to Earnings Ratio' : 'PE Percentile',
        'Price to Book Ratio' : 'PB Percentile',
        'Price to Sales Ratio' : 'PS Percentile',
        'EV / Ebitda' : 'EV / Ebitda Percentile',
        'EV / GP' : 'EV / GP Percentile'
    }

    for metric in metrics.keys():
        for row in df.index:
            df.loc[row, metrics[metric]] = stats.percentileofscore(df[metric], df.loc[row, metric])/100

    for index, row in df.iterrows():
        value_percentiles = [row[metrics[m]] for m in metrics.keys()]
        rv_score = mean(value_percentiles)
        df.loc[index, 'RV Score'] = rv_score
        
    return df

def main():
    stocks = get_sp500_constituents()
    base_df = base_dataframe(stocks)
    clean_df = clean_dataframe(base_df)
    final_df = calculate_percentiles(clean_df)

    final_df.sort_values('RV Score', ascending=True, inplace=True)

    total_value = portfolio_input()
    number_of_stocks = num_stocks_input()
    rv_final_portfolio = final_df[:number_of_stocks].copy()
    rv_final_portfolio.reset_index(drop=True ,inplace=True)

    position_size = float(total_value) / len(rv_final_portfolio.index)
    position_size

    rv_final_portfolio.loc[:, 'Number of Shares to Buy'] = (position_size / rv_final_portfolio['Price']).apply(math.floor)



if __name__ == '__main__':
    main()