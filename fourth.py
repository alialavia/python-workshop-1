"""
To evaluate the good or bad score of a tweet, we first tokenize the tweet, and then 
stemmize each word in our tweet. We also associate each stem with positive and negative values, 
respectively, using a dictionary.

Finally, we caculate the average word weight of a tweet, and decide if it's a good or bad one 
based on that.

"""

import nltk
from nltk.stem.porter import *

stemmer = PorterStemmer()

# Break down a string into words
def get_words(str):
    return nltk.word_tokenize(str)

# Iterate through the words in the tweet string
word_weights = { "thank": 1.0, "to": 0.0, "the": 0.0, "histor": 0.5, "cut": 0.0, "that": 0.0, 
"I": 0.0, "sign": 0.0, "into": 0.0, "law": 0.0, "your": 0.0, "paycheck": 0.0, "way": 0.0, "UP": 0.0, 
"your": 0.0, "way": 0.0, "down": 0.0, "and": 0.0, "america": 0.0, "is": 0.0, "onc": 0.0, "again": 0.0, 
"open": 0.0, "for": 0.0, "busi": 0.0}

# Calculate the average value of words in list_of_words
def get_average_word_weight(list_of_words):  
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
avg_tweet_weight = get_average_word_weight(words)

print ("The weight of the tweet is " + str(avg_tweet_weight))

if avg_tweet_weight > 0:
    print ("It's a good tweet")
else:
    print ("It's a bad tweet")
