# ExcelPlugin/modules/multi_excel.py

import pandas as pd
from openpyxl import Workbook
from typing import List, Tuple, Union, Dict, Optional
from ..utils.header import Header
from .excel import Excel

from pathlib import Path
MODULE_DIR = Path(__file__).parents[0] # Директория модуля
CURRENT_DIR = Path.cwd() # Текущая директория

class MultiExcel:
    def __init__(self):
        self._wb = Workbook()
        self._sheets:  Dict[str, Excel] = {}
        self._remove_default_sheet()

    @property
    def sheets(self):
        return list(self._sheets.keys())

    def _remove_default_sheet(self):
        if "Sheet" in self._wb.sheetnames:
            del self._wb["Sheet"]

    def __getitem__(self, key: str) -> Excel:
        return self._sheets[key]

    def rename_sheet(self, old_name: str, new_name: str):
        """_summary_

        Args:
            old_name (str): Старое имя листа
            new_name (str): Новое имя листа

        Raises:
            KeyError: Если лист уже отстутствует
        """
        if old_name not in self._sheets:
            raise KeyError(f"Sheet {old_name} not in Index")
        self._wb[old_name].title = new_name
        self._sheets[new_name] = self._sheets.pop(old_name) # Способ переименования ключей в словаре


    def add_sheet(
        self,
        data: pd.DataFrame,
        worksheet: str
    ) -> Excel:
        """Добавление нового листа
        :param data: DataFrame с данными
        :param worksheet: Имя листа
        :param header: Опциональный заголовок
        :raises ValueError: Если лист уже существует
        """
        if worksheet in self.sheets:
            raise ValueError(f"Sheet '{worksheet}' already exists")

        sheet = Excel(
            data=data,
            workbook=self._wb,
            worksheet=worksheet
        )
        self._sheets[worksheet] = sheet
        return sheet

    def save(self, filename: str, filepath: Union[str, None]=None):
        """Сохранение документа

        :param filename: Имя файла
        :param filepath: Путь для сохранения (по умолчанию - текущая директория)
        """
        for sheet in self._sheets.values():
            sheet._write_data()
        if filepath:
            self._wb.save(Path(filepath) / filename)
        else:
            self._wb.save(CURRENT_DIR / filename)
