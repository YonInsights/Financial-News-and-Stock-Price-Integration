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
