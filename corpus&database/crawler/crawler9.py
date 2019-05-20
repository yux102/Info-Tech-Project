
########completing the output of a list of all the title in one pdf

import pdfminer
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
import codecs

def parse_obj(objs):
    count = 0
    # print (objs)
    # print (len(objs))
    for i in range(len(objs)):
        # print ("hhhh", objs[i])
        if i > 3:
            if isinstance(objs[i], pdfminer.layout.LTFigure):
                count = count + 1
    # print (count)
    if count == 2:
        return True
    elif count > 2 and 6+count < len(objs):
        return True
    else:
        return False

def parse_obj_title(objs):
    for i in range(len(objs)):
        if i == 3:
            if isinstance(objs[i], pdfminer.layout.LTTextBox):
                for o in objs[i]._objs:
                    if isinstance(o,pdfminer.layout.LTTextLine):
                        text=o.get_text()
                        ######## print (text)
                        return text
                        # if o._objs.layout.LTChar.fontsize == 29.754:
                        #     print (o._objs.layout._text)
                        # if text.strip():
                        #     # print(o._objs._text)
                        #     for c in  o._objs:
                        #         if isinstance(c, pdfminer.layout.LTChar):
                        #             if c.fontsize == 29.754:
                        #                 # print (c._text)
                        #                 print("aaaa")
                        #             # print ("fontname %s"%c.fontname)
                        #             # print ("fontname %s"%c.fontsize)
            # if it's a container, recurse
            elif isinstance(objs[i], pdfminer.layout.LTFigure):
                parse_obj_title(objs[i]._objs)
            else:
                pass

def parse_obj_content(objs):
    new_text = ''
    count = 1
    for i in range(len(objs)):
        if i > 3 :
            if isinstance(objs[i], pdfminer.layout.LTTextBox):
                for o in objs[i]._objs:
                    if isinstance(o,pdfminer.layout.LTTextLine):
                        text=o.get_text()
                        # print (type(text.encode('ascii','ignore')))
                        text = text.encode('utf-8')
                        text = text[:-1]
                        # print (text)
                        # if text.encode('ascii','ignore') == 'COMP9444' or text.encode('ascii','ignore') == 'c(cid:13)Alan Blair, 2018' or text.encode('ascii','ignore') == 'c(cid:13)Alan Blair, 2013-19' or text.encode('ascii','ignore') == 'c(cid:13)Alan Blair, 2017-18' or text.encode('ascii','ignore') == 'c(cid:13)Alan Blair, 2013-18' or text.encode('ascii','ignore') == 'UNSW':
                        #     # new_text = new_text + ' '+ text
                        #     # print ("1111111111111")
                        #     break
                        if text == 'c(cid:13)AIMA, 2002, Alan Blair, 2010-9' or text == 'UNSW':
                            # new_text = new_text + ' '+ text
                            # print ("1111111111111")
                            break
                        if '(cid:4)' in text:
                            text = text.lstrip('(cid:4)')
                            if new_text == '':
                                new_text = str(count) + '.'+ text
                                count = int(count)+1
                            else:
                                new_text = new_text+' '+ str(count)+'.'+ text
                                count = int(count)+1
                        else:
                            if new_text == '':
                                new_text = text
                            else:
                                new_text = new_text + ' ' + text
                            # new_text = new_text + ' ' + text
    # print ("sajhdhsa",new_text)
                        # if o._objs.layout.LTChar.fontsize == 29.754:
                        #     print (o._objs.layout._text)
                        # if text.strip():
                        #     # print(o._objs._text)
                        #     for c in  o._objs:
                        #         if isinstance(c, pdfminer.layout.LTChar):
                        #             if c.fontsize == 29.754:
                        #                 # print (c._text)
                        #                 print("aaaa")
                        #             # print ("fontname %s"%c.fontname)
                        #             # print ("fontname %s"%c.fontsize)
            # if it's a container, recurse
            elif isinstance(objs[i], pdfminer.layout.LTFigure):
                parse_obj_title(objs[i]._objs)
            else:
                pass
    # print("adhjabjha",new_text)
    return new_text
filename = '7a_Logic.pdf'
document = open(filename, 'rb')
#Create resource manager
rsrcmgr = PDFResourceManager()
# Set parameters for analysis.
laparams = LAParams()
# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
pages = PDFPage.create_pages(document)
# interpreter.process_page(pages)

#page is the iterator of the pages, it is for one single page object
title = []
content = []
for page in PDFPage.get_pages(document):
    interpreter.process_page(page)
    layout = device.get_result()
    if layout.pageid > 1:
        # print ("aaa")
        if parse_obj(layout._objs) == True:
            text_title = parse_obj_title(layout._objs).encode('utf-8')
            text_title = text_title[:-1]
            title.append(text_title)
            text_content = parse_obj_content(layout._objs)
            text_content = text_content + ' (If you want to find more, please check in the lecture notes '+ filename +' Page ' + str(layout.pageid - 1) +' )'
            content.append(text_content)
            # # print (text_content)

for i in range(len(title)):
    print ("\n")
    print (title[i])
    print (content[i])
f1 = codecs.open('title0000.txt', 'w')
for i in title:
    f1.write(i)
    f1.write('\n')
f2 = codecs.open('content0000.txt', 'w')
for i in content:
    f2.write(i)
    f2.write('\n')