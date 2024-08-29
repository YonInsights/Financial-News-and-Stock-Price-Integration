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
