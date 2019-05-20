#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from preprocess import construct_corpus
from load_data import load_data
import numpy as np
import math




def ir_model(query):
    
    query = query
    
    corpus_sorted, features, idf, vocabulary, length_corpus, chunks_corpus_raw, title_corpus_raw, learning_factor, flat = load_data('corpus_data')
    
    query = [query]
    query = construct_corpus(query)
    query = query[0].split()
    
    
    total_term = 0
    tf = {}
    for x in query:
        if x in vocabulary:
            tf[x] = tf.setdefault(x , 0) + 1
            total_term += 1
    for x in tf:
        tf[x] = tf[x]/total_term
        
    tfidf = {}
    for x in tf:
        tfidf[x] = tf[x] * idf[vocabulary[x]]
    need_sqrt = 0
    for x in tfidf:
        need_sqrt += tfidf[x] * tfidf[x]
        
    sqrt = math.sqrt(need_sqrt)
    for x in tfidf:
        tfidf[x] = tfidf[x] / sqrt
        
    store = [tfidf]
    store = np.array(store)
    np.save('query_data.npy',store)
    
    dic_rank = {}
    for j in range(len(corpus_sorted)):
        chunk = corpus_sorted[j]
        query_tfidf = []
        chunk_tfidf = []
        theta = []
        for term in tfidf:
            if term in chunk:
                query_tfidf.append(tfidf[term])
                chunk_tfidf.append(chunk[term])
                theta.append(learning_factor[j][term])
        sum_multi = 0
        for i in range(len(query_tfidf)):
            sum_multi += query_tfidf[i] * chunk_tfidf[i] * theta[i]
            
        dic_rank[j] = sum_multi
        
        
    sorted_rank = sorted(dic_rank.items(), key = lambda x : x[1], reverse=True)
    if sorted_rank[0][1] < 0.05:
        return 'Sorry, we cannot find anything about your query. Do you have another question?'
    max_answer = 4
    result = [sorted_rank[i][0] + 1 for i in range(max_answer) if sorted_rank[i][1] != 0]

    for i in range(len(result)):
        if result[i] > length_corpus:
            result[i] -= length_corpus

        
    new_result = []
    for x in result:
        if x not in new_result:
            new_result.append(x)
    result = new_result
    answer_list = []
    for x in result:
        one_answer = title_corpus_raw[x-1] + ': ' + chunks_corpus_raw[x-1]
        answer_list.append(one_answer)
   
    result_index = {}
    for i in range(len(result)):
        result_index[i+1] = result[i] - 1 + length_corpus
        
    
    result_index = [result_index]
    result_index = np.array(result_index)
    np.save('result_index.npy',result_index)
        
    
    
    answer = ''
    for i in range(len(answer_list)):
        answer = answer + 'Suggested Answer ' + str(i+1) + ':\n' + answer_list[i] + '\n\n'
    if flat == True:
        answer = answer + 'Which was the best answer?\n(Feedback helps us improve the system.)\n'
    else:
        answer = answer + 'Which was the best answer?\n(Feedback helps us improve the system.)\n'
    return answer



                



    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
