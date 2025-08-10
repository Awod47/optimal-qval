import yfinance as yf
import pandas as pd

def base_dataframe(stocks_df):
    tickers = stocks_df['Ticker'].tolist()
    print('fetching data for your stocks')

    count = 0
    all_data = []

    for ticker in tickers:

        if count%50 == 0:
            print(f'currently getting data for stock {count+1}')
        ticker_data = yf.Ticker(ticker).info

        gp = ticker_data.get('grossProfits')
        ev = ticker_data.get('enterpriseValue')
        ev_gp = ev / gp if gp not in (None, 0) and ev not in (None, 0) else None

        all_data.append({
            'Ticker': ticker,
            'Price' : ticker_data.get('regularMarketPrice'),
            'Number of Shares to Buy' : 'N/A',
            'Price to Earnings Ratio' : ticker_data.get('trailingPE'),
            'PE Percentile' : 'N/A',
            'Price to Book Ratio' : ticker_data.get('priceToBook'),
            'PB Percentile' : 'N/A',
            'Price to Sales Ratio' : ticker_data.get('priceToSalesTrailing12Months'),
            'PS Percentile' : 'N/A',
            'EV / Ebitda' : ticker_data.get('enterpriseToEbitda'),
            'EV / Ebitda Percentile' : 'N/A',
            'EV / GP' : ev_gp,
            'EV / GP Percentile' : 'N/A',
            'RV Score' : 'N/A'
        })
        count+=1

    print('data fetch complete')
    base_df = pd.DataFrame(all_data)
    return base_df