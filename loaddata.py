from __future__ import division
import nltk
import glob
import os
import re
import numpy as np
from bs4 import BeautifulSoup
import lexicalFeatures
#Calling modules : lex = lexicalFeatures.lexical_features(raw3)
import bagofwords
#Calling modules : bag = bagofword.Bag_Of_Words(raw3)
import pos1
#Calling modules : pos = pos1.Part_of_Speech(raw3)


from nltk.tokenize import sent_tokenize,word_tokenize
from sklearn.feature_extraction import DictVectorizer
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import CountVectorizer
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
word_tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')


#Load Train Data

#from nltk.corpus import PlaintextCorpusReader
#corpus_root = 'C:\\Python27\\C50\\mytrain\\AaronPressman'
#wordlists = PlaintextCorpusReader(corpus_root, '.*')
#raw = wordlists.raw()
#wordlists.fileids()
#wordlists.sents()

#Print File and analyse one by one

#AaronPressman
file1 = open('C:\\Python27\\C50\\mytrain\\AaronPressman\\1.txt')
a1 = file1.read()

file2 = open('C:\\Python27\\C50\\mytrain\\AaronPressman\\2.txt')
a2 = file2.read()

file3 = open('C:\\Python27\\C50\\mytrain\\AaronPressman\\3.txt')
a3 = file3.read()

#AlanCrosby
file4 = open('C:\\Python27\\C50\\mytrain\\AlanCrosby\\1.txt')
b1 = file4.read()

file5 = open('C:\\Python27\\C50\\mytrain\\AlanCrosby\\2.txt')
b2 = file5.read()

file6 = open('C:\\Python27\\C50\\mytrain\\AlanCrosby\\3.txt')
b3 = file6.read()

#AlexanderSmith
file7 = open('C:\\Python27\\C50\\mytrain\\AlexanderSmith\\1.txt')
c1 = file7.read()

file8 = open('C:\\Python27\\C50\\mytrain\\AlexanderSmith\\2.txt')
c2 = file8.read()

file9 = open('C:\\Python27\\C50\\mytrain\\AlexanderSmith\\3.txt')
c3 = file9.read()

#BenjaminKangLim
file10 = open('C:\\Python27\\C50\\mytrain\\BenjaminKangLim\\1.txt')
d1 = file10.read()

file11 = open('C:\\Python27\\C50\\mytrain\\BenjaminKangLim\\2.txt')
d2 = file11.read()

file12 = open('C:\\Python27\\C50\\mytrain\\BenjaminKangLim\\3.txt')
d3 = file12.read()

#BernardHickey
file13 = open('C:\\Python27\\C50\\mytrain\\BernardHickey\\1.txt')
e1 = file13.read()

file14 = open('C:\\Python27\\C50\\mytrain\\BernardHickey\\2.txt')
e2 = file14.read()

file15 = open('C:\\Python27\\C50\\mytrain\\BernardHickey\\3.txt')
e3 = file15.read()


#Processing text,remove url

a1 = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', a1)
a2 = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', a2)
a3 = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', a3)

b1 = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', b1)
b2 = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', b2)
b3 = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', b3)

c1 = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', c1)
c2 = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', c2)
c3 = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', c3)

d1 = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', d1)
d2 = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', d2)
d3 = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', d3)

e1 = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', e1)
e2 = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', e2)
e3 = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', e3)

#print a1


#TestData1
file16 = open('C:\\Python27\\C50\\mytest\\authorB.txt')
z1 = file16.read()

#TestData2
file17 = open('C:\\Python27\\C50\\mytest\\authorE.txt')
z2 = file17.read()

#TestData3
file18 = open('C:\\Python27\\C50\\mytest\\authorC.txt')
z3 = file18.read()
    




        


