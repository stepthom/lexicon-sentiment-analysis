"""
Author: Stephen W. Thomas

Reformat the MPQA lexicon into an easier-to-parse format.
"""


# For doing cool regular expressions
import re

f = open('lexicon_easy.csv', 'w')

# Read in the lexicon. Here's an example line:
#
# type=weaksubj len=1 word1=abandoned pos1=adj stemmed1=n priorpolarity=negative
#
# For now, just use a regular expression to grab the word and the priorpolarity parts.
with open('subjclueslen1-HLTEMNLP05.tff', 'rb') as file:
    for line in file.readlines():
        print line
        m = re.search('.*word1=(\S+).*priorpolarity=(\S+)', line)

        score = 0
        if m.group(2) == 'positive':
            score = 1
        elif m.group(2) == 'negative':
            score = -1
        f.write("%s,%d\n" % (m.group(1), score))

f.close()
        