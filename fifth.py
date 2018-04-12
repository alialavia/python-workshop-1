"""
To evaluate the good or bad score of a tweet, we first tokenize the tweet, and then 
stemmize each word in our tweet. We also associate each stem with positive and negative values, 
respectively, using a dictionary.

Finally, we caculate the average word weight of a tweet, and decide if it's a good or bad one 
based on that.

"""
import json

from nltk import word_tokenize
from nltk.stem.porter import *

stemmer = PorterStemmer()

# Break down a string into words
def get_words(str):
    return word_tokenize(str)

# Initialize word weights and read them from word_weights.json
word_weights = {}
with open("word_weights.json") as f: # open the json file, and put its handler in variable f
    word_weights = json.load(f)      # read the content of the file into 

# Calculate the average value of words in list_of_words
def get_average_word_weight(list_of_words, word_weights):  
    number_of_words = len(list_of_words)
    sum_of_word_weights = 0.0  
    for w in list_of_words:
        stemmed_word = stemmer.stem(w)
        if stemmed_word in word_weights:
            sum_of_word_weights += word_weights[stemmed_word]
        else:
            print ('"' + stemmed_word + '": 0.0,')

    return sum_of_word_weights / number_of_words


tweet_string = "Thanks to the historic TAX CUTS that I signed into law, your paychecks are going way UP, your taxes are going way DOWN, and America is once again OPEN FOR BUSINESS!"

words = get_words(tweet_string)
avg_tweet_weight = get_average_word_weight(words, word_weights)

print ("The weight of the tweet is " + str(avg_tweet_weight))

if avg_tweet_weight > 0:
    print ("It's a good tweet")
else:
    print ("It's a bad tweet")
