"""
Author: Stephen W. Thomas

Perform sentiment analysis using the MPQA lexicon.

Note, in this simple approach, we don't do anything to handle negations
or any of the other hard problems.
"""


# For reading input files in CSV format
import csv

# For doing cool regular expressions
import re

# For sorting dictionaries
import operator

# Intialize an empty list to hold all of our tweets
tweets = []


# A helper function that removes all the non ASCII characters
# from the given string. Retuns a string with only ASCII characters.
def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)



# LOAD AND CLEAN DATA

# Load in the input file and process each row at a time.
# We assume that the file has three columns:
# 0. The tweet text.
# 1. The tweet ID.
# 2. The tweet publish date
#
# Create a data structure for each tweet:
#
# id:       The ID of the tweet
# pubdate:  The publication date of the tweet
# orig:     The original, unpreprocessed string of characters
# clean:    The preprocessed string of characters

with open('newtwitter.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    reader.next()
    for row in reader:

        tweet= dict()
        tweet['orig'] = row[0]
        tweet['id'] = int(row[1])
        tweet['pubdate'] = int(row[2])

        # Ignore retweets
        if re.match(r'^RT.*', tweet['orig']):
            continue

        tweet['clean'] = tweet['orig']

        # Remove all non-ascii characters
        tweet['clean'] = strip_non_ascii(tweet['clean'])

        # Normalize case
        tweet['clean'] = tweet['clean'].lower()

        # Remove the hashtag symbol
        tweet['clean'] = tweet['clean'].replace(r'#', '')

        tweets.append(tweet)

# Create a data structure to hold the lexicon.
# We will use a Python diction. The key of the dictionary will be the word
# and the value will be the word's score.
lexicon = dict()

# Read in the lexicon. 
with open('subjectivity_clues_hltemnlp05/lexicon_easy.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        lexicon[row[0]] = int(row[1])

# Use lexicon to score tweets
for tweet in tweets:
    score = 0
    for word in tweet['clean'].split():
        if word in lexicon:
            score = score + lexicon[word]

    tweet['score'] = score
    if (score > 0):
        tweet['sentiment'] = 'positive'
    elif (score < 0):
        tweet['sentiment'] = 'negative'
    else:
        tweet['sentiment'] = 'neutral'


# Print out summary stats
total = float(len(tweets))
num_pos = sum([1 for t in tweets if t['sentiment'] == 'positive'])
num_neg = sum([1 for t in tweets if t['sentiment'] == 'negative'])
num_neu = sum([1 for t in tweets if t['sentiment'] == 'neutral'])
print "Positive: %5d (%.1f%%)" % (num_pos, 100.0 * (num_pos/total))
print "Negative: %5d (%.1f%%)" % (num_neg, 100.0 * (num_neg/total))
print "Neutral:  %5d (%.1f%%)" % (num_neu, 100.0 * (num_neu/total))


# Print out some of the tweets
tweets_sorted = sorted(tweets, key=lambda k: k['score'])

print "\n\nTOP NEGATIVE TWEETS"
negative_tweets = [d for d in tweets_sorted if d['sentiment'] == 'negative']
for tweet in negative_tweets[0:10]:
    print "id=%d, score=%.2f, clean=%s" % (tweet['id'], tweet['score'], tweet['clean'])

print "\n\nTOP POSITIVE TWEETS"
positive_tweets = [d for d in tweets_sorted if d['sentiment'] == 'positive']
for tweet in positive_tweets[-10:]:
    print "id=%d, score=%.2f, clean=%s" % (tweet['id'], tweet['score'], tweet['clean'])

print "\n\nTOP NEUTRAL TWEETS"
neutral_tweets = [d for d in tweets_sorted if d['sentiment'] == 'neutral']
for tweet in neutral_tweets[0:10]:
    print "id=%d, score=%.2f, clean=%s" % (tweet['id'], tweet['score'], tweet['clean'])
