import pandas as pd

def combine_datasets(sentiment_path, stock_path, output_path, sentiment_key_column, stock_key_column):
    """
    Combines sentiment analysis data with stock data based on a common column.
    
    Parameters:
    sentiment_path (str): Path to the sentiment analysis CSV file.
    stock_path (str): Path to the stock data CSV file.
    output_path (str): Path to save the combined data.
    sentiment_key_column (str): The column in the sentiment data to join on.
    stock_key_column (str): The column in the stock data to join on.
    """
    try:
        # Load datasets
        df_sentiment = pd.read_csv(sentiment_path)
        df_stock = pd.read_csv(stock_path)

        # Print the first few rows and columns of each DataFrame
        print("Sentiment DataFrame:")
        print(df_sentiment.head())
        print("Columns in Sentiment DataFrame:", df_sentiment.columns)
        
        print("Stock DataFrame:")
        print(df_stock.head())
        print("Columns in Stock DataFrame:", df_stock.columns)

        # Rename columns to align the key columns if necessary
        if sentiment_key_column != stock_key_column:
            df_sentiment.rename(columns={sentiment_key_column: stock_key_column}, inplace=True)

        # Ensure the key_column exists in both DataFrames
        if stock_key_column not in df_sentiment.columns:
            raise ValueError(f"Key column '{stock_key_column}' not found in sentiment data.")
        if stock_key_column not in df_stock.columns:
            raise ValueError(f"Key column '{stock_key_column}' not found in stock data.")

        # Combine datasets
        df_combined = pd.merge(df_sentiment, df_stock, on=stock_key_column, how='inner')

        # Check if the combined DataFrame is empty
        if df_combined.empty:
            print("The combined DataFrame is empty. No matching rows found.")

        # Save combined data
        df_combined.to_csv(output_path, index=False)
        print(f"Combined data saved to {output_path}")

    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except ValueError as e:
        print(f"Value error: {e}")
    except Exception as e:
        print(f"Error combining datasets: {e}")

if __name__ == "__main__":
    sentiment_path = r'D:\10 Academy_Kifya\Week 1\Financial-News-and-Stock-Price-Integration\Data\processed_analyst_ratings.csv'
    stock_path = r'D:\10 Academy_Kifya\Week 1\Financial-News-and-Stock-Price-Integration\Data\yfinance_data\AAPL_historical_data.csv'  # Example file
    output_path = r'D:\10 Academy_Kifya\Week 1\Financial-News-and-Stock-Price-Integration\Data\combined_data.csv'
    sentiment_key_column = 'date'  # Column name in the sentiment data
    stock_key_column = 'Date'  # Column name in the stock data

    combine_datasets(sentiment_path, stock_path, output_path, sentiment_key_column, stock_key_column)
