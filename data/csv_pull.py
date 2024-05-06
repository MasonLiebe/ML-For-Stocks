import pandas as pd
import csv

# GETTING DATA FROM CSV FILES
data_dir = "../data/"

stock_files = [
    "AMD.csv", "BTC-USD.csv", "ETH-USD.csv", "FSV.csv",
    "GOOG.csv", "INFY.csv", "KNX.csv", "META.csv",
    "NVDA.csv", "TSLA.csv", "TSM.csv", "UNH.csv"
]

dataframes = {}
# Loop through the file names, loading each into a separate dataframe
for file_name in stock_files:
    # Construct the full path to the file
    file_path = data_dir + file_name
    # Load the CSV file into a dataframe and store it in the dictionary
    df = pd.read_csv(file_path)
    
    # Check if 'Close' column exists
    if 'Close' in df.columns:
        # Calculate normalized growth based on the 'Close' price
        initial_close = df['Close'].iloc[0]
        df['Normalized Growth'] = df['Close'] / initial_close
    
    # Store the dataframe back in the dictionary
    dataframes[file_name[:-4]] = df