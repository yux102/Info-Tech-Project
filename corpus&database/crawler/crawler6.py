#
# ########completing the output of a list of all the title in one pdf
#
# import pdfminer
# from pdfminer.layout import LAParams
# from pdfminer.converter import PDFPageAggregator
# from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure
# from pdfminer.pdfpage import PDFPage
# from pdfminer.pdfinterp import PDFResourceManager
# from pdfminer.pdfinterp import PDFPageInterpreter
#
# def parse_obj(objs):
#     count = 0
#     # print (objs)
#     # print (len(objs))
#     for i in range(len(objs)):
#         # print ("hhhh", objs[i])
#         if i > 3:
#             if isinstance(objs[i], pdfminer.layout.LTFigure):
#                 count = count + 1
#     # print (count)
#     if count == 2:
#         return True
#     elif count > 2 and 6+count < len(objs):
#         return True
#     else:
#         return False
#
# def parse_obj_title(objs):
#     for i in range(len(objs)):
#         if i == 3:
#             if isinstance(objs[i], pdfminer.layout.LTTextBox):
#                 for o in objs[i]._objs:
#                     if isinstance(o,pdfminer.layout.LTTextLine):
#                         text=o.get_text()
#                         ######## print (text)
#                         return text
#                         # if o._objs.layout.LTChar.fontsize == 29.754:
#                         #     print (o._objs.layout._text)
#                         # if text.strip():
#                         #     # print(o._objs._text)
#                         #     for c in  o._objs:
#                         #         if isinstance(c, pdfminer.layout.LTChar):
#                         #             if c.fontsize == 29.754:
#                         #                 # print (c._text)
#                         #                 print("aaaa")
#                         #             # print ("fontname %s"%c.fontname)
#                         #             # print ("fontname %s"%c.fontsize)
#             # if it's a container, recurse
#             elif isinstance(objs[i], pdfminer.layout.LTFigure):
#                 parse_obj_title(objs[i]._objs)
#             else:
#                 pass
#
# def parse_obj_content(objs):
#     new_text = ''
#     count = 1
#     for i in range(len(objs)):
#         if i > 3 :
#             if isinstance(objs[i], pdfminer.layout.LTTextBox):
#                 for o in objs[i]._objs:
#                     if isinstance(o,pdfminer.layout.LTTextLine):
#                         text=o.get_text()
#                         # print (type(text.encode('ascii','ignore')))
#                         text = text.encode('ascii','ignore')
#                         text = text[:-1]
#                         # print ('11111',text)
#                         if text.encode('ascii','ignore') == 'COMP9444' or text.encode('ascii','ignore') == 'c(cid:13)Alan Blair, 2018' or text.encode('ascii','ignore') == 'c(cid:13)Alan Blair, 2013-19' or text.encode('ascii','ignore') == 'c(cid:13)Alan Blair, 2017-18' or text.encode('ascii','ignore') == 'cAlan Blair, 2017-18' or text.encode('ascii','ignore') == 'UNSW':
#                             # print ('111',text)
#                             # new_text = new_text + ' '+ text
#                             # print ("1111111111111")
#                             break
#                         if '(cid:4)' or '!' in text:
#                             text = text.lstrip('!')
#                             if new_text == '':
#                                 new_text = str(count) + '.'+ text
#                                 count = int(count)+1
#                                 # print ('a',new_text)
#                             else:
#                                 new_text = new_text+' '+ str(count)+'.'+ text
#                                 count = int(count)+1
#                                 # print ('b',new_text)
#                         else:
#                             if new_text == '':
#                                 new_text = text
#                                 # print ('c',new_text)
#                             else:
#                                 new_text = new_text + ' ' + text
#                                 # print('d',new_text)
#                             # new_text = new_text + ' ' + text
#     # print ("sajhdhsa",new_text)
#                         # if o._objs.layout.LTChar.fontsize == 29.754:
#                         #     print (o._objs.layout._text)
#                         # if text.strip():
#                         #     # print(o._objs._text)
#                         #     for c in  o._objs:
#                         #         if isinstance(c, pdfminer.layout.LTChar):
#                         #             if c.fontsize == 29.754:
#                         #                 # print (c._text)
#                         #                 print("aaaa")
#                         #             # print ("fontname %s"%c.fontname)
#                         #             # print ("fontname %s"%c.fontsize)
#             # if it's a container, recurse
#             elif isinstance(objs[i], pdfminer.layout.LTFigure):
#                 parse_obj_title(objs[i]._objs)
#             else:
#                 pass
#     # print("adhjabjha",new_text)
#     return new_text
#
# document = open('15_Coevolution.pdf', 'rb')
# #Create resource manager
# rsrcmgr = PDFResourceManager()
# # Set parameters for analysis.
# laparams = LAParams()
# # Create a PDF page aggregator object.
# device = PDFPageAggregator(rsrcmgr, laparams=laparams)
# interpreter = PDFPageInterpreter(rsrcmgr, device)
# pages = PDFPage.create_pages(document)
# # interpreter.process_page(pages)
#
# #page is the iterator of the pages, it is for one single page object
# title = []
# content = []
# for page in PDFPage.get_pages(document):
#     interpreter.process_page(page)
#     layout = device.get_result()
#     if layout.pageid > 1:
#         # print ("aaa")
#         if parse_obj(layout._objs) == True:
#             text_title = parse_obj_title(layout._objs).encode('ascii','ignore')
#             text_title = text_title[:-1]
#             title.append(text_title)
#             text_content = parse_obj_content(layout._objs)
#             content.append(text_content)
#             # print (text_content)
# print(title)
# print(content)
# with open('title.txt','w') as f:
#     for i in title:
#         f.write(i)
#         f.write('\n')
# with open('content.txt','w') as f:
#     for i in content:
#         f.write(i)
#         f.write('\n')


######upload to the database
import json
import  pymongo
with open('title.txt','r') as f:
    title_txt = f.readlines()
    title_txt = ''.join(title_txt)
    title_txt = title_txt.split('\n')
    title_txt = title_txt[:-1]
with open('answer_content.txt','r') as f:
    answer = f.readlines()
    answer = ''.join(answer)
    answer = answer.split('\n')
    answer = answer[:-1]
# print (title_txt)
print (answer)
print (len(answer))
####### dict=[]
with open('corpus.json', 'w') as f:
    for i in range(len(title_txt)):
        corpus = {}
        corpus[title_txt[i]] = answer[i]
        # dict.append(corpus)
        json.dump(corpus,f)
##### print (dict)
myclient = pymongo.MongoClient("mongodb://Lalala_0704:sophia950704@ds123698.mlab.com:23698/test_0704")
db = myclient.get_database()
collection = db['comp9444corpus']
for i in range(len(title_txt)):
    corpus = {}
    with open('comp9414corpus.json', 'w') as f:
        corpus[title_txt[i]] = answer[i]
        # dict.append(corpus)
        json.dump(corpus,f)
        collection.insert_one(corpus)
#









        # print(corpus)
#############
# for i in range(len(title)):
#     print ("\n")
#     print (title[i])
#     print (content[i])
# # print (title)
# print (len(title))
# #
# # print (content)
# print (len(content))

