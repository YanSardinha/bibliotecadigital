import json
import re
import requests


# assigns a JSON string to a variable called coder

with open('C:/Users/yan.sardinha/Desktop/Projetinhos/bibliotecadigital/dados_biblioteca_link_arquivos.json', 'r') as file:

    data = json.load(file)

'''
CAMPOS
'Id'
'Titulo'
'NomeDoCurso'
'NomeOrientador'
'LinkArquivo'
'Autores' ---> 'Autores':[{'Tipo': Principal,'Nome', Valério}] -----> ['Autores'][0]['Tipo']

Olhando na coluna LinkArquivo é possível verificar que há arquivos com extensão .pdf , .docx e .doc
'''


for i in data:
    url = i['LinkArquivo']
    print(f"Id: {i ['Id']}, url: {url}")
    try:
        extension = re.search('\.(docx|pdf|doc)$', url).group()
    except:
        print(f'Extensão diferente de PDF, DOCX ou DOC: {url}')
    try:
        response = requests.get(i['LinkArquivo'], allow_redirects=True, verify=False)
        print(f'Status code: {response.status_code}')
        if response.status_code == 200:
            open(f"tccs/{i['Id']}{extension}", "wb").write(response.content)
    except:
        print(f'Algum erro aconteceu:  {response.status_code}')