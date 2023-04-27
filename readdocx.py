import json
import os
import docx2txt

begin = 'AGRADECIMENTOS'
end = ['LISTA', 'SUMÁRIO', 'RESUMO', '“TALVEZ NÃO TENHA']
data_file_path = 'C:/Users/yan.sardinha/Desktop/Projetinhos/bibliotecadigital/bibliotecadigital/dados_biblioteca_link_arquivos.json'
tccs_dir_path = 'C:/Users/yan.sardinha/Desktop/Projetinhos/bibliotecadigital/bibliotecadigital/tccs'
dict_data = {}

with open(data_file_path) as data_file:
    dict_data = json.load(data_file)

for id in range(3710):
    file_path = os.path.join(tccs_dir_path, f"{id}.docx")
    if not os.path.exists(file_path):
        print(f'File does not exist for id = {id}')
        continue

    try:
        document = docx2txt.process(file_path)
        upper = document.upper()

        try:
            idx1 = document.find(begin)
            idx2 = len(document)
            for i in end:
                if upper.find(i.upper()) > 0 and upper.find(i.upper()) < idx2:
                    idx2 = document.find(i)
            if idx1 > 0:
                print(f'Found "AGRADECIMENTOS" on id = {id}')
                res = document[idx1 + len(begin) + 1:idx2]
                striped = res.strip()
                dict_data[id]['Agradecimentos'] = striped
                print(f"Agradecimentos on id = {id}: {striped}")
        except Exception as e:
            continue

        if 'Agradecimentos' not in dict_data[id]:
            print(f'"AGRADECIMENTOS" not found on id = {id}')

    except Exception as e:
        print(f'Error occurred while processing file for id = {id}: {str(e)}')
        break
 
with open(data_file_path, 'w') as data_file:
    json.dump(dict_data, data_file, indent=4)
