import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure the sentiment_analysis module is found
sys.path.append('D:/10 Academy_Kifya/Week 1/Financial-News-and-Stock-Price-Integration/scripts')
from sentiment_analysis import add_sentiment_scores

def save_processed_data(df, output_path):
    """
    Saves the DataFrame with sentiment scores to a CSV file.
    
    Parameters:
    df (pd.DataFrame): The DataFrame with sentiment scores.
    output_path (str): The path where the CSV file will be saved.
    """
    try:
        df.to_csv(output_path, index=False)
        print(f"Processed data saved to {output_path}")
    except Exception as e:
        print(f"Error saving processed data: {e}")

def main():
    # Load data
    input_path = r'D:\10 Academy_Kifya\Week 1\Financial-News-and-Stock-Price-Integration\Data\raw_analyst_ratings.csv'
    try:
        df_ratings = pd.read_csv(input_path)
        print(f"Data loaded successfully from {input_path}")
        print(f"First few rows:\n{df_ratings.head()}")
    except FileNotFoundError:
        print(f"File not found: {input_path}")
        return
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Apply sentiment analysis
    try:
        df_ratings = add_sentiment_scores(df_ratings)
        print(f"Sentiment analysis applied. First few rows:\n{df_ratings.head()}")
    except Exception as e:
        print(f"Error applying sentiment analysis: {e}")
        return

    # Define output path
    output_path = r'D:\10 Academy_Kifya\Week 1\Financial-News-and-Stock-Price-Integration\Data\processed_analyst_ratings.csv'
    
    # Save the processed data
    save_processed_data(df_ratings, output_path)

    # Check if file is saved
    if pd.io.common.file_exists(output_path):
        print(f"Processed data file exists at {output_path}")
    else:
        print(f"File not found after saving: {output_path}")

    # Descriptive statistics of sentiment
    print(df_ratings['Sentiment'].describe())

    # Plot sentiment distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df_ratings['Sentiment'], kde=True)
    plt.title('Distribution of Sentiment Scores')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    main()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define file paths
combined_data_path = r'D:\10 Academy_Kifya\Week 1\Financial-News-and-Stock-Price-Integration\Data\combined_data.csv'

def load_and_inspect_data(file_path):
    """
    Loads the combined data from a CSV file and returns a DataFrame.
    """
    try:
        df_combined = pd.read_csv(file_path)
        print("Data loaded successfully.")
        print(df_combined.head())
        print(df_combined.describe())
        return df_combined
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error loading data: {e}")

def plot_sentiment_vs_stock_price(df):
    """
    Plots Sentiment vs. Stock Price.
    """
    if df is not None:
        plt.figure(figsize=(12, 6))
        sns.scatterplot(x='Sentiment', y='StockPrice', data=df)  # Replace 'StockPrice' with your column name
        plt.title('Sentiment vs. Stock Price')
        plt.xlabel('Sentiment Score')
        plt.ylabel('Stock Price')
        plt.show()

def plot_time_series(df):
    """
    Plots time series of Stock Prices and Sentiment Scores.
    """
    if df is not None:
        # Convert 'Date' to datetime if necessary
        df['Date'] = pd.to_datetime(df['Date'])  # Replace 'Date' with your date column

        # Plot Stock Prices over Time
        plt.figure(figsize=(14, 7))
        sns.lineplot(x='Date', y='StockPrice', data=df)
        plt.title('Stock Prices Over Time')
        plt.xlabel('Date')
        plt.ylabel('Stock Price')
        plt.xticks(rotation=45)
        plt.show()

        # Plot Sentiment Score over Time
        plt.figure(figsize=(14, 7))
        sns.lineplot(x='Date', y='Sentiment', data=df)
        plt.title('Sentiment Score Over Time')
        plt.xlabel('Date')
        plt.ylabel('Sentiment Score')
        plt.xticks(rotation=45)
        plt.show()

if __name__ == "__main__":
    df_combined = load_and_inspect_data(combined_data_path)
    plot_sentiment_vs_stock_price(df_combined)
    plot_time_series(df_combined)
