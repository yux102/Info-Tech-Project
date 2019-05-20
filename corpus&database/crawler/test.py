import pdfminer
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal

import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

# # Open a PDF document.
# fp = open('01_Neuroanatomy.pdf', 'rb')
# parser = PDFParser(fp)
# document = PDFDocument(parser)
#
# # Get the outlines of the document.
# outlines = document.get_outlines()
# for (level,title,dest,a,se) in outlines:
#     print (level, title)
def parse_obj_title(objs):
    for obj in objs:
        if isinstance(obj, pdfminer.layout.LTTextBox):
            for o in obj._objs:
                if isinstance(o,pdfminer.layout.LTTextLine):
                    text=o.get_text()
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
        elif isinstance(obj, pdfminer.layout.LTFigure):
            parse_obj_title(obj._objs)
        else:
            pass
document = open('01_Neuroanatomy.pdf', 'rb')
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
    ####### print(layout)
    ####### how to print title#######  print (layout._objs[3].get_text())
    ####### print(layout._objs)
    ####### print (type(layout._objs))
    parse_obj_title(layout._objs)


#     layout = device.get_result()
#     for element in layout:
#         if isinstance(element, LTTextBox):
#             element.get_text()



# # receive the LTPage object for the page.
# layout = device.get_result()
# for element in layout:
#     if isinstance(element, LTTextBox):
#         print(element.get_text())


# basic usage
# from pdfminer.pdfparser import PDFParser
# from pdfminer.pdfdocument import PDFDocument
# from pdfminer.pdfpage import PDFPage
# from pdfminer.pdfpage import PDFTextExtractionNotAllowed
# from pdfminer.pdfinterp import PDFResourceManager
# from pdfminer.pdfinterp import PDFPageInterpreter
# from pdfminer.pdfdevice import PDFDevice
#
# # Open a PDF file.
# fp = open('01_Neuroanatomy.pdf', 'rb')
# # Create a PDF parser object associated with the file object.
# parser = PDFParser(fp)
# # Create a PDF document object that stores the document structure.
# # Supply the password for initialization.
# document = PDFDocument(parser)
# # Check if the document allows text extraction. If not, abort.
# if not document.is_extractable:
#     raise PDFTextExtractionNotAllowed
# # Create a PDF resource manager object that stores shared resources.
# rsrcmgr = PDFResourceManager()
# # Create a PDF device object.
# device = PDFDevice(rsrcmgr)
# # Create a PDF interpreter object.
# interpreter = PDFPageInterpreter(rsrcmgr, device)
# # Process each page contained in the document.
# for page in PDFPage.create_pages(document):
#     interpreter.process_page(page)
