
pip install vaderSentiment

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sentiment = SentimentIntensityAnalyzer()


text_1 = "the movie was the best movie ever"
text_2 =  "The pizza tastes so terrible."
text_3 = ""

sent_1 = sentiment.polarity_scores(text_1)
sent_2 = sentiment.polarity_scores(text_2)
sent_3 = sentiment.polarity_scores(text_3)

print("Sentiment of text 1:", sent_1)
print("Sentiment of text 2:", sent_2)
print("El sentimiento del texto 3 es:", sent_3)
