from textblob import TextBlob
import pandas as pd

def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given text using TextBlob.
    
    Parameters:
    text (str): The text to analyze.
    
    Returns:
    float: The polarity of the text (-1 to 1).
    """
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def add_sentiment_scores(df):
    """
    Applies sentiment analysis to the headlines in the DataFrame.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing headlines.
    
    Returns:
    pd.DataFrame: The DataFrame with an added 'Sentiment' column.
    """
    # Replace 'headline' with the actual column name if it differs
    df['Sentiment'] = df['headline'].apply(analyze_sentiment)  
    return df
def save_processed_data(df, output_path):
    """
    Saves the DataFrame with sentiment scores to a CSV file.
    
    Parameters:
    df (pd.DataFrame): The DataFrame with sentiment scores.
    output_path (str): The path where the CSV file will be saved.
    """
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")

if __name__ == "__main__":
    # Load data
    input_path = r'D:\10 Academy_Kifya\Week 1\Financial-News-and-Stock-Price-Integration\Data\raw_analyst_ratings.csv'
    df_ratings = pd.read_csv(input_path)

    # Apply sentiment analysis
    df_ratings = add_sentiment_scores(df_ratings)

    # Define output path
    output_path = r'D:\10 Academy_Kifya\Week 1\Financial-News-and-Stock-Price-Integration\Data\processed_analyst_ratings.csv'

    # Save the processed data
    save_processed_data(df_ratings, output_path)