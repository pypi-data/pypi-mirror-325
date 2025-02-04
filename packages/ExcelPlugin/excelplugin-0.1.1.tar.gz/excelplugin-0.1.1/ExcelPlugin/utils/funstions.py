# ExcelPlugin.utils.functions.py

def get_column_letter(letter_idx: int) -> str:
    """Переводит число в номер столбца Excel."""
    column = ""
    while letter_idx > 0:
        letter_idx -= 1
        column = chr(letter_idx % 26 + ord('A')) + column
        letter_idx //= 26
    return column
