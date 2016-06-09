from __future__ import division
import nltk
import glob
import os
import re
import numpy as np
from bs4 import BeautifulSoup

from nltk.tokenize import sent_tokenize,word_tokenize
from sklearn.feature_extraction import DictVectorizer
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import CountVectorizer
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
word_tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')


#Create lexical features
#Normalizing text : set(w.lower() for w in text
#Lexical diversity measure the richness of the vocabulary ~get how many % of the total number of words
def lexical_features(text):

    tokens    = nltk.word_tokenize(text.lower())
    words     = word_tokenizer.tokenize(text.lower())
    sentences = sentence_tokenizer.tokenize(text)
    vocab     = set(words)
    lexical   = ( len(vocab) / len(words))
    words_per_sentence = np.array([len(word_tokenizer.tokenize(s)) for s in sentences ])
    #words_per_sentence = np.array(len(words)/len(sentences))
    
    #average number of words per sentence
    avg_words  = words_per_sentence.mean()
    
    #sentence length variation
    sent_len   = words_per_sentence.std()
 
    #average = sum(len(word) for word in words)/len(words)
   

    print 'Sentences :'
    print(sentences)
    print 'Token :'
    print(tokens)
    print 'Words :'
    print (words)
    print 'Vocabualry: '
    print (vocab)
    print 'Lexical Diversity :'
    print (lexical)
    print 'average number of words per sentence :'
    print ( avg_words)
    print 'sentence length variation :'
    print (sent_len)



    # Commas per sentence
    comma = tokens.count(',') / float(len(sentences))
    
    # Semicolons per sentence
    semicolon = tokens.count(';') / float(len(sentences))
    
    # Colons per sentence
    colon = tokens.count(':') / float(len(sentences))

    print ' Commas per sentence :'
    print(comma)
    print ' Semicolons per sentence :'
    print (semicolon)
    print ' Colons per sentence :'
    print(colon)
    
'''
def token_to_pos(text):
    
    words  = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(words)
    print tagged
        
    pos_list = ['NN', 'NNP', 'DT', 'IN', 'JJ', 'NNS']
    sss = np.array([[text.count(tagged) for tagged in pos_list]
                           for tagged in tagged]).astype(np.float64)
'''




    










    
