# HTML Table to JSON Converter

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

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/html-table-to-json.git
   cd html-table-to-json
   ```

2. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   ```

3. Ative o ambiente virtual:

   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para converter uma tabela de um arquivo HTML para JSON, siga os passos abaixo:

1. Navegue até o diretório `src`:

   ```bash
   cd src
   ```

2. Execute o script `main.py` passando o caminho do arquivo HTML como argumento:

   ```bash
   python main.py caminho/para/seu/arquivo.html
   ```

3. O JSON resultante será salvo em `output/out.json`.

### Exemplo

Se você tem um arquivo HTML chamado `tabela.html` na raiz do projeto, execute:

```bash
python main.py ../tabela.html
```

O JSON será salvo em `output/out.json` e os logs serão armazenados em `logs/html_table_to_json.log`.

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
