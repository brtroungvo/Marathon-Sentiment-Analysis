from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from data.read_json import comments

analyzer = SentimentIntensityAnalyzer()

# Print out each comment and their polarity scores
for sentence in comments:
    vs = analyzer.polarity_scores(sentence)
    print(f"{sentence} \n|---> {str(vs)} \n{'-'*50}")
