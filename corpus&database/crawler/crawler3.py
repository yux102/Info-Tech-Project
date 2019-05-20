
########completing the output of a list of all the title in one pdf

import pdfminer
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter


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
document = open('08_Recurrent.pdf', 'rb')
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
    ####### print(layout)
    ####### how to print title#######  print (layout._objs[3].get_text())
    ####### print(layout._objs)
    ####### print (type(layout._objs))
        # print(layout._objs[3].get_text().encode('utf-8'))

        text_title = parse_obj_title(layout._objs).encode('ascii','ignore')
        text_title = text_title[:-1]
        title.append(text_title)
print (title)

