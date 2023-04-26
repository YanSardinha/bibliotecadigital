'''
Método - Para Extração de PDF's

Foi utilizado o PyPDF2 com a função de PdfReader na qual é possível 
passar para uma variável uma lista (que seriam as páginas) com o 
texto de cada página contido dentro de um PDF, e assim foi possivel, 
utilizando as funcionalidade padrões do python para encontrar onde 
se encontram os  agradecimentos de cada TCC.
'''

from PyPDF2 import PdfReader
import json

begin = 'AGRADECIMENTOS'
sum = -1
id = 0
dict = {}
with open('C:/Users/yan.sardinha/Desktop/Projetinhos/bibliotecadigital/bibliotecadigital/dados_biblioteca_link_arquivos.json') as file:
    dict = json.load(file)

while id < 3710:
    try:
        reader = PdfReader(f"C:/Users/yan.sardinha/Desktop/Projetinhos/bibliotecadigital/bibliotecadigital/tccs/{id}.pdf")
        number_of_pages = len(reader.pages)
        i=0 
        
        while i < number_of_pages:
            page = reader.pages[i]
            text = page.extract_text()
            i+=1
            try:
                idx1 = text.find(begin)
                if idx1 > 0:
                    print(f'Opening a file to write, id = {id}')
                    res = text[idx1 + len(begin) + 1:]
                    striped = res.strip()
                    dict[id]['Agradecimentos'] = striped
                    sum += id
                    print('File closed')
            except:
                print(f'Nothing to be found on id = {id}')
                break
    except:
        print(f'File does not exists, file id = {id}')
    
    if sum < 0:
        print(f'"Agradecimentos" not found on id = {id}')
        
    id += 1

with open('C:/Users/yan.sardinha/Desktop/Projetinhos/bibliotecadigital/bibliotecadigital/dados_biblioteca_link_arquivos.json', 'w') as file:
    json.dump(dict, file, indent=4)


'''
for obj in dict:
    print(obj)
    obj['Agradecimentos'] = 'NovoValor'

with open('C:/Users/yan.sardinha/Desktop/Projetinhos/bibliotecadigital/bibliotecadigital/dados_biblioteca_link_arquivos_agrad.json', 'w') as f:
    json.dump(dict, f)

print('New file successfully genereted.')

'''




