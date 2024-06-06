# Conversor de Tabela HTML para JSON

![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
![pandas](https://img.shields.io/badge/pandas-1.x-yellow.svg)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.x-green.svg)

## Descrição

Este projeto é um conversor que lê uma tabela de um arquivo HTML e a transforma em um arquivo JSON. Ele utiliza as bibliotecas `pandas` e `BeautifulSoup` para realizar a conversão de maneira eficiente e estruturada. O projeto segue princípios de Clean Architecture, Clean Code e SOLID, garantindo um código modular, legível e fácil de manter.

## Estrutura do Projeto

```
html-table-to-json/
├── src/
│   ├── main.py
│   ├── services/
│   │   ├── html_parser.py
│   │   ├── json_converter.py
│   │   └── file_handler.py
│   └── utils/
│       └── logger.py
├── requirements.txt
├── README.md
├── LICENSE.md
└── .gitignore
```

## Instalação

### Pré-requisitos

- Python 3.6 ou superior
- Pip (gerenciador de pacotes do Python)

### Passos

1. Instale o pacote via pip:

   ```bash
   pip install html-table-to-json
   ```

## Uso

Para converter uma tabela de um arquivo HTML para JSON, siga os passos abaixo:

1. Importe a função `convert_html_table_to_json` no seu script:

   ```python
   from html_table_to_json import convert_html_table_to_json
   ```

2. Use a função `convert_html_table_to_json`, passando o caminho do arquivo HTML como argumento:

   ```python
   json_data = convert_html_table_to_json("caminho/para/seu/arquivo.html")
   ```

3. O JSON resultante pode ser usado diretamente no seu script ou salvo em um arquivo.

### Exemplo

Se você tem um arquivo HTML chamado `tabela.html` na raiz do projeto, você pode convertê-lo da seguinte forma:

```python
from html_table_to_json import convert_html_table_to_json

json_data = convert_html_table_to_json("../tabela.html")

with open("output/out.json", "w") as outfile:
    outfile.write(json_data)
```

## Estrutura do Código

### `main.py`

Ponto de entrada do programa. Coordena a leitura do arquivo HTML, parsing, conversão e escrita do JSON de saída.

### `services/file_handler.py`

Contém funções para leitura e escrita de arquivos.

### `services/html_parser.py`

Contém funções para parsing do HTML utilizando BeautifulSoup.

### `services/json_converter.py`

Contém funções para converter a tabela HTML para JSON utilizando Pandas.

### `utils/logger.py`

Configura e inicializa o logger para registrar eventos importantes e erros.

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Faça um push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.

## Contato

Para mais informações, entre em contato pelo email [thiagoarturschumann@gmail.com](mailto:thiagoarturschumann@gmail.com).
