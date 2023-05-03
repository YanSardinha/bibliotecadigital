
# BibliotecaDigital
Utilizando python para fazer download de pdfs encontrados em um arquivo json para que seja feita a leitura dos dados dentro do pdf e extrair as informações desejadas.


## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/YanSardinha/bibliotecadigital
```

Entre no diretório do projeto

```bash
  cd bibliotecadigital
```

Instale as dependências

```bash
  pip install -r requirements.txt
```

Vale lembrar que, ao ler os pdfs, o arquivo json é carregado como uma lista, então o debug que aparece ao executar não necessariamente está relacionado com o id do tcc.

## Aprendizados

Aprendi como extrair dados de um PDF usando a biblioteca PyPDF2 em Python. Utilizei essa biblioteca para extrair informações de páginas de PDFs e salvá-las em um arquivo JSON. E também a importância de lidar com erros e exceções ao manipular arquivos em Python.

Em resumo, aprendi que é possível extrair informações úteis de PDFs usando Python e bibliotecas como PyPDF2, e que a programação defensiva é uma prática importante ao lidar com arquivos em Python, uma vez que problemas como arquivos inacessíveis ou corrompidos podem ocorrer.

Extrair todas as informações de arquivos .doc e .docx utilizando apenas o Python e suas bibliotecas pode ser um desafio. Embora existam bibliotecas como o python-docx e o textract que permitem a extração de texto de arquivos .doc e .docx, nem todas as informações contidas nesses arquivos podem ser facilmente extraídas.

Além disso, algumas informações podem estar contidas em formatos não suportados pelas bibliotecas de extração de texto, como fórmulas matemáticas e equações. Nesses casos, pode ser necessário recorrer a bibliotecas especializadas ou a softwares específicos para realizar a extração dessas informações.

Embora seja possível extrair muitas informações de arquivos .doc e .docx usando apenas o Python e suas bibliotecas, nem todas as informações podem ser facilmente extraídas. É importante estar ciente das limitações das bibliotecas de extração de texto e avaliar se é necessário utilizar outras ferramentas para extrair todas as informações desejadas.


## Autores

- [@YanSardinha](https://www.github.com/YanSardinha)


# License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/YanSardinha/bibliotecadigital/blob/main/LICENSE)

