#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 20:10:40 2019

@author: hal
"""

from load_data import load_data
import numpy as np
import re


def update(feedback):
    feedback = feedback
    
    result_index = load_data('result_index')
    if result_index == False:
        return 'Sorry, you have not asked a question about course content.'
    key = [str(x) for x in result_index]
    
    corpus_sorted, features, idf, vocabulary, length_corpus, chunks_corpus_raw, title_corpus_raw, learning_factor, flat = load_data('corpus_data')
    dic_query_tfidf = load_data('query_data')
    if dic_query_tfidf == False:
        return 'Sorry, you have not asked a question about course content.'
    
    feedback = re.sub('[^0-9]', '', feedback)
    if feedback in key:
        if feedback == '1':
            return 'Thanks for your feedback. Do you have other questions?'
        else:
            feedback = int(feedback)
            update_chunk_index = result_index[feedback]
            update_chunk = learning_factor[update_chunk_index]
            #whcih is a dict
            for x in dic_query_tfidf:
                if x in update_chunk:
                    update_chunk[x] = update_chunk[x] * (1 + dic_query_tfidf[x])
            store = [corpus_sorted, features, idf, vocabulary, length_corpus, chunks_corpus_raw, title_corpus_raw, learning_factor]
            store = np.array(store)
            np.save('corpus_data.npy',store)
            if flat == True:
                return 'Thanks for your feedback. Do you have other questions?'
            else:
                return 'Thanks for your feedback. Do you have other questions I can help with?'
            
            
            
            
    else:
        return 'Sorry, your input is invalid. Do you want to try again or do you have other questions?'
    