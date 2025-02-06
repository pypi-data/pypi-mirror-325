# ExcelPlugin

![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)
![License](https://img.shields.io/pypi/l/ExcelPlugin)
![PyPI Version](https://img.shields.io/pypi/v/ExcelPlugin)

## Features

- 🎨 Advanced cell styling (fonts, borders, alignment)
- 📊 Seamless pandas DataFrames integration
- 🔄 Excel template processing
- 📈 Batch operations support
- 🖥️ CLI interface for quick operations

## Installation

```bash
pip install ExcelPlugin
```

## Quick Start

```python
from ExcelPlugin import MultiExcel

# Создаем объекты DataFrame
df_2 = pd.DataFrame()
df_1 = pd.DataFrame()

multi = MultiExcel() # Создаем объект MultiExcel

# Добавляем страницы 
multi.add_sheet(df, 'data_1')  # Добавляем страницу 'data_1' и DataFrame
multi.add_sheet(df, 'data_1')  

# Создаем шапку Excel документа
multi['data_1'].add_header()  # Обязательно нужно вызвать метод add_header() для создания заголовков.
# Если передать в add_header() аргументы -> получим многоуровневый заголовки
multi['data_2'].add_header()

# Форматируем столбцы 
multi['data_1'].set_money_column(MONEY_COLUMN: Union[List[str], None]=None)  
multi['data_1'].set_percent_column(PERCENT_COLUMN: Union[List[str], None]=None)  
multi['data_1'].set_date_column(DATE_COLUMN: Union[List[str], None]=None) 

# Переименование страниц Excel
multi.rename_sheet(old_name='data_1', new_name='new_data_1') 

multi.save(filename=fr"{filename_email}" + ".xlsx", filepath=filepath)  # Сохраняем файл

```

## CLI Usage

```bash
# Apply template styles
excel-plugin apply-styles --input data.xlsx --template styles.json --output styled.xlsx

# Convert CSV to styled Excel
excel-plugin csv2xlsx data.csv --output report.xlsx
```

## Documentation

Full documentation available at [GitHub Wiki](https://github.com/yourusername/ExcelPlugin/wiki)

## Contributing

Pull requests are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.