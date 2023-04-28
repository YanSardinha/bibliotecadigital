import win32com.client

word = win32com.client.Dispatch("Word.Application")
word.visible = True

wb = word.Documents.Open("C:/Users/yan.sardinha/Documents/GitHub/bibliotecadigital/tccs/101.doc")
doc = word.ActiveDocument
print(doc.Range().text)