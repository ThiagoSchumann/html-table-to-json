# HTML Table to JSON Converter

[Leia em Português](README-pt.md)

![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
![pandas](https://img.shields.io/badge/pandas-1.x-yellow.svg)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.x-green.svg)

## Description

This project is a converter that reads a table from an HTML file and transforms it into a JSON file. It uses the `pandas` and `BeautifulSoup` libraries to perform the conversion efficiently and in a structured manner. The project follows Clean Architecture, Clean Code, and SOLID principles, ensuring modular, readable, and maintainable code.

## Project Structure

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

## Installation

### Prerequisites

- Python 3.6 or higher
- Pip (Python package manager)

### Steps

1. Install the package via pip:

   ```bash
   pip install html-table-to-json
   ```

## Usage

To convert a table from an HTML file to JSON, follow these steps:

1. Import the `convert_html_table_to_json` function in your script:

   ```python
   from html_table_to_json import convert_html_table_to_json
   ```

2. Use the `convert_html_table_to_json` function, passing the path of the HTML file as an argument:

   ```python
   json_data = convert_html_table_to_json("path/to/your/file.html")
   ```

3. The resulting JSON can be used directly in your script or saved to a file.

### Example

If you have an HTML file named `table.html` in the root of the project, you can convert it as follows:

```python
from html_table_to_json import convert_html_table_to_json

json_data = convert_html_table_to_json("../table.html")

with open("output/out.json", "w") as outfile:
    outfile.write(json_data)
```

## Code Structure

### `main.py`

Entry point of the program. Coordinates reading the HTML file, parsing, conversion, and writing the output JSON.

### `services/file_handler.py`

Contains functions for reading and writing files.

### `services/html_parser.py`

Contains functions for parsing HTML using BeautifulSoup.

### `services/json_converter.py`

Contains functions for converting the HTML table to JSON using Pandas.

### `utils/logger.py`

Configures and initializes the logger to record important events and errors.

## Contribution

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for more details.

## Contact

For more information, contact via email at [thiagoarturschumann@gmail.com](mailto:thiagoarturschumann@gmail.com).
