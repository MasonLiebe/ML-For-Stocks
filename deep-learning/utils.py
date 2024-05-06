#  This file contains utility functions for the project.
import numpy as np
import pandas as pd
import yfinance as yf

def fetch_stock_data(tickers, start_date=None, end_date=None, interval='1d'):
    """
    Fetches historical stock data for given tickers using yfinance.
    
    Parameters:
    - tickers (list of str): List of stock ticker symbols.
    - start_date (str): Start date for the data in format 'YYYY-MM-DD' (optional).
    - end_date (str): End date for the data in format 'YYYY-MM-DD' (optional).
    - interval (str): Data interval. Valid intervals: '1d', '1wk', '1mo', etc.

    Returns:
    - dict: A dictionary with tickers as keys and DataFrames as values.
    """
    stock_data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date, end=end_date, interval=interval)
        stock_data[ticker] = data
    
    return stock_data


# Compute additional metrics
def compute_metrics(data):
    """
    Computes additional metrics for stock data.
    
    Parameters:
    - data (dict): A dictionary with tickers as keys and DataFrames as values.
    
    Returns:
    - dict: A dictionary with tickers as keys and DataFrames as values.
    """
    metrics = {}
    for ticker, df in data.items():
        # Calculate daily return
        df['Daily Return'] = df['Close'].pct_change().fillna(0)
        
        # Calculate cumulative return
        df['Cumulative Return'] = (1 + df['Daily Return']).cumprod().fillna(1)
        
        # Calculate simple moving averages for specified periods
        df['SMA_3'] = df['Close'].rolling(window=3).mean()
        df['SMA_7'] = df['Close'].rolling(window=7).mean()
        df['SMA_30'] = df['Close'].rolling(window=30).mean()  # Approximating 1 month
        df['SMA_90'] = df['Close'].rolling(window=90).mean()  # Approximating 3 months
        
        # Calculate VWAP (Volume Weighted Average Price)
        if 'Volume' in df.columns:
            df['VWAP'] = (df['Close'] * df['Volume']).cumsum() / df['Volume'].cumsum()
            df['VWAP_3'] = (df['Close'] * df['Volume']).rolling(window=3).sum() / df['Volume'].rolling(window=3).sum()
            df['VWAP_7'] = (df['Close'] * df['Volume']).rolling(window=7).sum() / df['Volume'].rolling(window=7).sum()
            df['VWAP_30'] = (df['Close'] * df['Volume']).rolling(window=30).sum() / df['Volume'].rolling(window=30).sum()
            df['VWAP_90'] = (df['Close'] * df['Volume']).rolling(window=90).sum() / df['Volume'].rolling(window=90).sum()
        
        metrics[ticker] = df
    
    return metrics