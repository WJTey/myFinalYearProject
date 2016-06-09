'''
The process of classifying words into their parts-of-speech and labeling them accordingly
is known as part-of-speech tagging, POS tagging, or simply tagging. Partsof-
speech are also known as word classes or lexical categories. The collection of tags
used for a particular task is known as a tagset.
'''

import nltk
import numpy as np
from collections import Counter

file2 = open('C:\\Python27\\C50\\mytrain\\AaronPressman\\2.txt')
raw2 = file2.read()


def Part_of_Speech(text):

    token = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(token)
    print tagged
    
    print [(word, tag) for word, tag in tagged if tag in ('NN','NNP','DT','IN','JJ','NNS')]
    counts = Counter(tag for word,tag in tagged if tag in ('NN','NNP','DT','IN','JJ','NNS'))
    print (counts)


    total = sum(counts.values())
    print dict((word, float(count)/total) for word,count in counts.items())
    print " \n "

'''
def findtags(tag_prefix,tagged_text):
    cfd = nltk.ConditionalFreqDist((tag,word))for (word,tag) in tagged_text
                    if tag.startwith((tag_prefix))
        return dict((
'''
