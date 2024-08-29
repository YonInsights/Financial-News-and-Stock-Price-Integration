import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: Loaded DataFrame.
    """
    return pd.read_csv(file_path)

def merge_data(df_ratings, df_stocks):
    """
    Merges sentiment analysis data with stock data on the 'date' column.
    
    Parameters:
    df_ratings (pd.DataFrame): DataFrame containing sentiment scores.
    df_stocks (pd.DataFrame): DataFrame containing stock data.
    
    Returns:
    pd.DataFrame: Merged DataFrame.
    """
    # Convert 'date' columns to datetime format
    df_ratings['date'] = pd.to_datetime(df_ratings['date'])
    df_stocks['date'] = pd.to_datetime(df_stocks['date'])
    
    # Merge on 'date'
    df_merged = pd.merge(df_ratings, df_stocks, on='date', how='inner')
    
    return df_merged

def save_data(df, file_path):
    """
    Save DataFrame to a CSV file.
    
    Parameters:
    df (pd.DataFrame): DataFrame to save.
    file_path (str): The path to save the CSV file.
    """
    df.to_csv(file_path, index=False)
