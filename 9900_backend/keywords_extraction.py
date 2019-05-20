#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 23:36:46 2019

@author: hal
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from preprocess import construct_corpus
import numpy as np


import  pymongo





def keywords_extracted_tfidf():
    
    
    
    myclient = pymongo.MongoClient("mongodb://Lalala_0704:sophia950704@ds123698.mlab.com:23698/test_0704")
    db = myclient.get_database()
    collection = [db['comp9414corpus'], db['comp9444corpus'], db['comp1531corpus']]
    title = []
    content = []
    for i in range(3):
        data = collection[i].find()
        final_dict = []
        for item in data:
            item.pop('_id')
            final_dict.append(item)
        for element in final_dict:
            for key in element:
                title.append(key)
        for element in final_dict:
            for key in element.values():
                content.append(key)
    
    #list : title and content
    chunks_corpus_raw = content
    
    chunks_corpus = construct_corpus(chunks_corpus_raw)

    title_corpus_raw = title
    
    titles_corpus = construct_corpus(title_corpus_raw)
    
    chunks_titles_corpus = []
    for i in range(len(chunks_corpus)):
        chunks_titles_corpus.append(chunks_corpus[i] + 1 * (' ' + titles_corpus[i]))
         
    corpus = titles_corpus + chunks_titles_corpus
    length_corpus = len(chunks_corpus)

    
    

    vectorizer = TfidfVectorizer(smooth_idf = False)
    corpus_matrix = vectorizer.fit_transform(corpus)
    corpus_matrix = corpus_matrix.toarray()
    
    features = vectorizer.get_feature_names()
    idf = vectorizer.idf_
    vocabulary = vectorizer.vocabulary_
    len_features = len(features)
    corpus_sorted = []
    for one_corpus in corpus_matrix:
        dic_corpus = {}
        for i in range(len_features):
            if one_corpus[i] > 0.15:
                dic_corpus[features[i]] = one_corpus[i]
                
        sorted_dic_corpus = dict(sorted(dic_corpus.items(), key = lambda x : x[1], reverse=True))
        corpus_sorted.append(sorted_dic_corpus)
    
    
    index = -1
    learning_factor = []
    for l in corpus_sorted:
        index += 1
        dic = {}
        for d in l:
            if 'outline' in l:
                dic[d] = 0
            elif index < length_corpus:
                dic[d] = 0.5
            else:
                dic[d] = 1
        learning_factor.append(dic)
    
    store = [corpus_sorted, features, idf, vocabulary, length_corpus, chunks_corpus_raw, title_corpus_raw, learning_factor]
    store = np.array(store)
    np.save('corpus_data.npy',store)
    
    return 'Restart Successfully'
    
    
   