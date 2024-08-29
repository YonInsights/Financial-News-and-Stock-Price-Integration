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
        # Ensure the sentiment column is available
        if 'Sentiment' in df.columns and 'stock' in df.columns:
            plt.figure(figsize=(12, 6))
            sns.scatterplot(x='Sentiment', y='stock', data=df)  # Replace 'stock' if needed
            plt.title('Sentiment vs. Stock Price')
            plt.xlabel('Sentiment Score')
            plt.ylabel('Stock Price')
            plt.show()
        else:
            print("Sentiment or stock columns are missing in the DataFrame.")

def plot_time_series(df):
    """
    Plots time series of Stock Prices and Sentiment Scores.
    """
    if df is not None:
        # Convert 'date' to datetime if necessary
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'])  # Convert to datetime

            # Plot Stock Prices over Time
            if 'stock' in df.columns:
                plt.figure(figsize=(14, 7))
                sns.lineplot(x='date', y='stock', data=df)  # Replace 'stock' with actual price column if needed
                plt.title('Stock Prices Over Time')
                plt.xlabel('Date')
                plt.ylabel('Stock Price')
                plt.xticks(rotation=45)
                plt.show()

            # Plot Sentiment Score over Time
            if 'Sentiment' in df.columns:
                plt.figure(figsize=(14, 7))
                sns.lineplot(x='date', y='Sentiment', data=df)
                plt.title('Sentiment Score Over Time')
                plt.xlabel('Date')
                plt.ylabel('Sentiment Score')
                plt.xticks(rotation=45)
                plt.show()
        else:
            print("Date column is missing in the DataFrame.")

if __name__ == "__main__":
    df_combined = load_and_inspect_data(combined_data_path)
    plot_sentiment_vs_stock_price(df_combined)
    plot_time_series(df_combined)
