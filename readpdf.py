'''
Primeiro Método
from pdfquery import PDFQuery

pdf = PDFQuery('C:/Users/yan.sardinha/Desktop/Projetinhos/bibliotecadigital/tccs/3.pdf')

pdf.load()
pdf.tree.write('customers.xml', pretty_print = True)
pdf
'''

'''
Segundo Método
'''

from PyPDF2 import PdfReader

reader = PdfReader("C:/Users/yan.sardinha/Desktop/Projetinhos/bibliotecadigital/tccs/3.pdf")
number_of_pages = len(reader.pages)
i=0 
file = open('C:/Users/yan.sardinha/Desktop/Projetinhos/bibliotecadigital/test.txt', 'w', encoding='UTF-8')
while i < number_of_pages:
    page = reader.pages[i]
    text = page.extract_text()
    i+=1
    file.write(text)

file.close()