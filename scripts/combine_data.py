import pandas as pd

# Load datasets
df_ratings = pd.read_csv(r'D:\10 Academy_Kifya\Week 1\Financial-News-and-Stock-Price-Integration\Data\processed_analyst_ratings.csv')
df_stock = pd.read_csv(r'D:\10 Academy_Kifya\Week 1\Financial-News-and-Stock-Price-Integration\Data\raw_stock_data.csv')

# Merge datasets
df_combined = pd.merge(df_ratings, df_stock, on='common_column', how='inner')  # Replace 'common_column' with the actual column name

# Save the combined data
df_combined.to_csv(r'D:\10 Academy_Kifya\Week 1\Financial-News-and-Stock-Price-Integration\Data\combined_data.csv', index=False)

import pandas as pd

def combine_datasets(sentiment_path, stock_path, output_path, key_column):
    """
    Combines sentiment analysis data with stock data based on a common column.
    
    Parameters:
    sentiment_path (str): Path to the sentiment analysis CSV file.
    stock_path (str): Path to the stock data CSV file.
    output_path (str): Path to save the combined data.
    key_column (str): The column to join on.
    """
    try:
        # Load datasets
        df_sentiment = pd.read_csv(sentiment_path)
        df_stock = pd.read_csv(stock_path)

        # Combine datasets
        df_combined = pd.merge(df_sentiment, df_stock, on=key_column, how='inner')

        # Save combined data
        df_combined.to_csv(output_path, index=False)
        print(f"Combined data saved to {output_path}")

    except Exception as e:
        print(f"Error combining datasets: {e}")

if __name__ == "__main__":
    sentiment_path = r'D:\10 Academy_Kifya\Week 1\Financial-News-and-Stock-Price-Integration\Data\processed_analyst_ratings.csv'
    stock_path = r'D:\10 Academy_Kifya\Week 1\Financial-News-and-Stock-Price-Integration\Data\raw_stock_data.csv'
    output_path = r'D:\10 Academy_Kifya\Week 1\Financial-News-and-Stock-Price-Integration\Data\combined_data.csv'
    key_column = 'common_column'  # Replace with the actual column name you want to merge on

    combine_datasets(sentiment_path, stock_path, output_path, key_column)
