from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    # Create an instance of SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()
    
    # Get sentiment scores
    sentiment_scores = sia.polarity_scores(text)
    
    return sentiment_scores
