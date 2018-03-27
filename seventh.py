"""
To evaluate the good or bad score of a tweet, we first tokenize the tweet, and then 
stemmize each word in our tweet. We also associate each stem with positive and negative values, 
respectively, using a dictionary.

Finally, we caculate the average word weight of a tweet, and decide if it's a good or bad one 
based on that.

"""
import json
import html
import twitter
import time

from nltk import word_tokenize, pos_tag
from nltk.stem.porter import *

# Break down a string into words
def get_words(str):
	useful_pos = {'NN'}
	tokens = word_tokenize(str)
	tags = pos_tag(tokens)
	return [word for word, pos in tags if pos in useful_pos] 

missing_words = {}

# Calculate the average value of words in list_of_words
def get_average_word_weight(list_of_words, word_weights):
	number_of_words = len(list_of_words)
	sum_of_word_weights = 0.0
	print (number_of_words)
	if number_of_words == 0:
		return 0.0
	stemmer = PorterStemmer()
	# Iterate through the words in the tweet string
	for w in list_of_words:
	    stemmed_word = stemmer.stem(w)
	    if stemmed_word in word_weights:
	        sum_of_word_weights += word_weights[stemmed_word]
	    else:
	        missing_words[stemmed_word] = 0.0

	return sum_of_word_weights / number_of_words

def anaylse_tweet(tweet_string, word_weights):
	words = get_words(tweet_string)
	avg_tweet_weight = get_average_word_weight(words, word_weights)
	print (tweet_string + ":" + str(avg_tweet_weight))

# Read tweets from an outside source
def load_json(json_file):
	with open(json_file) as f:
		return json.load(f)


word_weights = load_json("word_weights.json")
credentials = load_json(".cred.json")

api = twitter.Api(consumer_key=credentials["consumer_key"],
				  consumer_secret=credentials["consumer_secret"],
                  access_token_key=credentials["access_token_key"],
                  access_token_secret=credentials["access_token_secret"],
                  tweet_mode='extended')

statuses = api.GetUserTimeline(screen_name="realDonaldTrump", count=10)
for status in statuses:
	anaylse_tweet(html.unescape(status.full_text), word_weights)
	prev_status = status.full_text

print (missing_words)