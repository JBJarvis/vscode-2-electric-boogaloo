from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#Initiate VADER
sia = SentimentIntensityAnalyzer()

#Analyze sentiment of news headlines for selected topics
headline = "Apple announces new product","Tesla shipping results"
sentiment_scores = sia.polarity_scores(headline)

#and Print dat shit
print(sentiment_scores)