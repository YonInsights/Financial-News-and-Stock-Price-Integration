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
