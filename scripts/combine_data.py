import pandas as pd

# Define file paths
sentiment_file_path = 'D:/10 Academy_Kifya/Week 1/Financial-News-and-Stock-Price-Integration/Data/processed_analyst_ratings.csv'
stock_file_path = 'D:/10 Academy_Kifya/Week 1/Financial-News-and-Stock-Price-Integration/Data/yfinance_data/AAPL_historical_data.csv'
output_file_path = 'D:/10 Academy_Kifya/Week 1/Financial-News-and-Stock-Price-Integration/Data/combined_data.csv'

# Load the datasets
sentiment_df = pd.read_csv(sentiment_file_path)
stock_df = pd.read_csv(stock_file_path)

# Inspect the first few rows to determine the date format
print("Sentiment DataFrame Date Column:")
print(sentiment_df['Date'].head())
print("Stock DataFrame Date Column:")
print(stock_df['Date'].head())

# Convert Date columns to datetime format
try:
    # Specify format with timezone offset for sentiment data
    sentiment_df['Date'] = pd.to_datetime(sentiment_df['Date'], format='%Y-%m-%d %H:%M:%S%z', errors='coerce')
    # For stock data, no time zone, so use default format
    stock_df['Date'] = pd.to_datetime(stock_df['Date'], format='%Y-%m-%d', errors='coerce')
except Exception as e:
    print(f"Error converting date columns: {e}")

# Clean up column names
sentiment_df.columns = sentiment_df.columns.str.strip()
stock_df.columns = stock_df.columns.str.strip()

# Inspect unique dates
print("Sentiment Dates:")
print(sentiment_df['Date'].unique())
print("Stock Dates:")
print(stock_df['Date'].unique())

# Merge DataFrames
combined_df = pd.merge(sentiment_df, stock_df, on='Date', how='inner')

# Check combined DataFrame
print("Combined DataFrame:")
print(combined_df.head())

# Save combined DataFrame
combined_df.to_csv(output_file_path, index=False)
