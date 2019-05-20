# with open ('title_content.txt','r') as f:
#     for line in f:
#         print (line.strip('\n'))
#     all = f.readlines()
#     number = len(all)
# print (number)

# for i in range(number):
# with open ('title_content.txt','r') as f_1:
#         for line_1 in f_1:
#             corpus = {}
#             # title = f.readline()
#             title = line_1.strip('\n')
#             with open('answer_content.txt', 'r') as f_2:
#                 for line_2 in f_2:
#                     # answer = f_2.readline()
#                     answer = answer.strip('\n')
#                     corpus[title]=answer
#                     print (corpus)


import json
import  pymongo
with open('title_content.txt','r') as f:
    title = f.readlines()
    title = ''.join(title)
    title = title.split('\n')
    title = title[:-1]
with open('answer_content.txt','r') as f:
    answer = f.readlines()
    answer = ''.join(answer)
    answer = answer.split('\n')
    answer = answer[:-1]
# dict=[]
with open('corpus.json', 'w') as f:
    for i in range(len(title)):
        corpus = {}
        corpus[title[i]] = answer[i]
        # dict.append(corpus)
        json.dump(corpus,f)
# print (dict)
myclient = pymongo.MongoClient("mongodb://Lalala_0704:sophia950704@ds123698.mlab.com:23698/test_0704")
db = myclient.get_database()
collection = db['corpus']
# with open('corpus.json','r') as f:
#     data = json.load(f)
# collection.insert_one(data)
with open('data.json','r') as f:
    data = json.load(f)
    print (data)
collection.insert(data)