import sys
sys.path.append('D:/10 Academy_Kifya/Week 1/Financial-News-and-Stock-Price-Integration/scripts')
import pandas as pd
from sentiment_analysis import add_sentiment_scores
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df_ratings = pd.read_csv('D:/10 Academy_Kifya/Week 1/Financial-News-and-Stock-Price-Integration/Data/raw_analyst_ratings.csv')

# Apply sentiment analysis
df_ratings = add_sentiment_scores(df_ratings)

# Descriptive statistics of sentiment
print(df_ratings['Sentiment'].describe())

# Plot sentiment distribution
plt.figure(figsize=(10, 6))
sns.histplot(df_ratings['Sentiment'], kde=True)
plt.title('Distribution of Sentiment Scores')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()

import pandas as pd
from sentiment_analysis import add_sentiment_scores

def save_processed_data(df, output_path):
    """
    Saves the DataFrame with sentiment scores to a CSV file.
    
    Parameters:
    df (pd.DataFrame): The DataFrame with sentiment scores.
    output_path (str): The path where the CSV file will be saved.
    """
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")

def main():
    # Load data
    input_path = r'D:\10 Academy_Kifya\Week 1\Financial-News-and-Stock-Price-Integration\Data\raw_analyst_ratings.csv'
    df_ratings = pd.read_csv(input_path)

    # Apply sentiment analysis
    df_ratings = add_sentiment_scores(df_ratings)

    # Define output path
    output_path = r'D:\10 Academy_Kifya\Week 1\Financial-News-and-Stock-Price-Integration\Data\processed_analyst_ratings.csv'

    # Save the processed data
    save_processed_data(df_ratings, output_path)

if __name__ == "__main__":
    main()
