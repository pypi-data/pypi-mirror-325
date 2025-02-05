# ExcelPlugin.utils.formatter.py

# ExcelPlugin/utils/formatters.py

from openpyxl.cell import Cell
from typing import Union


def format_money(data, col_name, worksheet):
    for row in range(1, len(data) + 1):
        worksheet[f'{col_name}{row}'].number_format = '# ### ##0.00 ₽'

def format_percent(data, col_name, worksheet):
    for row in range(1, len(data) + 1):
        worksheet[f'{col_name}{row}'].number_format = '#0.00 %'


def format_date(data, col_name, worksheet) -> None:
    """Форматирует ячейку как дату."""
    for row in range(1, len(data) + 1):
        worksheet[f'{col_name}{row}'].number_format = 'dd.mm.yyyy'


def format_custom(cell: Cell, format_str: str) -> None:
    """Применяет произвольный числовой формат."""
    cell.number_format = format_str

def format_wrap_text(cell: Cell) -> None:
    """Включает перенос текста для ячейки."""
    cell.alignment = cell.alignment.copy(wrapText=True)
