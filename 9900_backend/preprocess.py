#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 23:34:09 2019

@author: hal
"""

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')


def construct_corpus(corpus_raw):
    new_stopwords = set(stopwords.words('english')) | set(['something', 'yes', 'no'])
    
    corpus = []
    lemmatizer = WordNetLemmatizer()
    for x in corpus_raw:
        one = re.sub('[^a-zA-Z]', ' ', x)
        one = one.lower()
        one = one.split()
        one = [lemmatizer.lemmatize(word, pos='n') for word in one if not word in new_stopwords]
        one = [lemmatizer.lemmatize(word, pos='v') for word in one]
        one = ' '.join(one)
        corpus.append(one)
        
    return corpus