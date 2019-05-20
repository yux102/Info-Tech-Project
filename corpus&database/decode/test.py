import json
import  pymongo
with open('title1111.txt','r',encoding='utf-8') as f:
    title_txt = f.readlines()
    title_txt = ''.join(title_txt)
    title_txt = title_txt.split('\n')
    title_txt = title_txt[:-1]

with open('content1111.txt','r',encoding='utf-8') as f:
    answer = f.readlines()
    answer = ''.join(answer)
    answer = answer.split('\n')
    answer = answer[:-1]
# if '' in title_txt:
#     print("aaaa")
# if '' in answer:
#     print("bbbbbb")
for i in range(len(title_txt)):
    print('\n')
    print(title_txt[i])
    print(answer[i])
print(len(title_txt))
print(len(answer))
# with open('corpus.json', 'w',encoding='utf-8') as f:
#     for i in range(len(title_txt)):
#         corpus = {}
#         corpus[title_txt[i]] = answer[i]
#         # dict.append(corpus)
#         json.dump(corpus,f,ensure_ascii=False)
# # ##### print (dict)
myclient = pymongo.MongoClient("mongodb://Lalala_0704:sophia950704@ds123698.mlab.com:23698/test_0704")
db = myclient.get_database()
collection = db['comp9414corpus']
for i in range(len(title_txt)):
    corpus = {}
    with open('corpus.json', 'w',encoding='utf-8') as f:
        corpus[title_txt[i]] = answer[i]
        # dict.append(corpus)
        json.dump(corpus,f,ensure_ascii=False)
        collection.insert_one(corpus)
# #####################
# data = collection.find()
# final_dict = []
# for item in data:
#     item.pop('_id')
#     final_dict.append(item)
# title = []
# content = []
# for element in final_dict:
#     for key in element:
#         title.append(key)
# for element in final_dict:
#     for key in element.values():
#         content.append(key)
# print(title)
# print(content)
# print(len(title))
# print(len(content))

