from __future__ import division
import nltk 
from nltk.tokenize import sent_tokenize,word_tokenize

import numpy as np
import nltk
import glob
import os

file3 = open('C:\\Python27\\C50\\mytrain\\AaronPressman\\1.txt')
raw3 = file3.read()

print "Creating the bag of words...\n"
from sklearn.feature_extraction.text import CountVectorizer


def Bag_Of_Words(text):

   # get most common words in the whole book
    NUM_TOP_WORDS = 5
    #NUM_TOP_WORDS = 10
    all_tokens = nltk.word_tokenize(text)
    fdist = nltk.FreqDist(all_tokens)
    vocab = fdist.keys()[:NUM_TOP_WORDS]

    # use sklearn to create the bag for words feature vector for each chapter
    vectorizer = CountVectorizer(vocabulary=vocab, tokenizer=nltk.word_tokenize)
    print (vectorizer)
    
    #fvs_bow = vectorizer.fit_transform(text).toarray().astype(np.float64)
    #print (fvs_bow)
   
    # normalise by dividing each row by its Euclidean norm
    #fvs_bow /= np.c_[np.apply_along_axis(np.linalg.norm, 0, fvs_bow)]

    #return fvs_bow

    #print (fvs_bow)
    

