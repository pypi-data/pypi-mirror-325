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
from ExcelPlugin import ExcelStyler, PandasExcelManager

# Create styled workbook
styler = ExcelStyler()
workbook = styler.create_workbook()
sheet = styler.add_sheet(workbook, "Report")

# Apply styles
styler.apply_style(sheet['A1'], 
                 font=styler.font(bold=True, color="FF0000"),
                 fill=styler.fill(patternType="solid", fgColor="00FF00"))

# Save
styler.save(workbook, "report.xlsx")

# Pandas integration
manager = PandasExcelManager()
df = manager.read_excel("data.xlsx")
manager.write_with_styles(df, "output.xlsx", styler)
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