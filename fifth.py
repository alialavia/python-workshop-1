"""
To evaluate the good or bad score of a tweet, we count the number of good and
bad words in it.

if a word is good, increase the value of good_words by one
else if a word is bad, increase the value of bad_words by one
if good_words > bad_words then it's a good tweet otherwise it's a bad tweet

"""
import json
import nltk
from nltk.stem.porter import *

stemmer = PorterStemmer()

# Break down a string into words
def get_words(str):
	return nltk.word_tokenize(str)

# Calculate the average value of words in list_of_words
def get_average_word_weight(list_of_words, word_weights):
	number_of_words = len(list_of_words)
	sum_of_word_weights = 0.0
	if number_of_words == 0:
		return 0.0
	# Iterate through the words in the tweet string
	for w in list_of_words:
	    stemmed_word = stemmer.stem(w)
	    if stemmed_word in word_weights:
	        sum_of_word_weights += word_weights[stemmed_word]
	    #else:
	        #print ('"' + stemmed_word + '": 0.0,')

	return sum_of_word_weights / number_of_words

def anaylse_tweet(tweet_string, word_weights):
	words = get_words(tweet_string)
	avg_tweet_weight = get_average_word_weight(words, word_weights)
	print ("The weight of the tweet is " + str(avg_tweet_weight))

	if avg_tweet_weight > 0:
		print ("It's a good tweet")
	else:
		print ("It's a bad tweet")

# Read tweets from an outside source
def read_from_files(json_file, tweet_file):
	word_weights = {}
	with open(json_file) as f:
		s = f.read()
		word_weights = json.loads(s)

	with open(tweet_file) as f:
		for tweet in f:
			print(tweet)
			anaylse_tweet(tweet, word_weights)
			print("----------------------")

read_from_files("word_weights.json", "tweets.txt")

