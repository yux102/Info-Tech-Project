from PyPDF2 import PdfFileReader
def getPdfContent(filename):
    pdf = PdfFileReader(open(filename, "rb"))
    content = ""
    for i in range(0,pdf.getNumPages()):
        pageObj = pdf.getPage(i)
        try:
            extractedText = pageObj.extractText()
            content += extractedText + "\n"
        except BaseException:
            pass
    return content.encode("ascii", "ignore")


with open("test.txt","w") as f:
    count=0
    for item in str(getPdfContent("01_Neuroanatomy.pdf")).split(" "):
        if item[-1]==".":
            f.write(item+"\n")
            count=0
        else:
            f.write(item+" ")
            count +=1
        if count==10:
            f.write("\n")
            count = 0
