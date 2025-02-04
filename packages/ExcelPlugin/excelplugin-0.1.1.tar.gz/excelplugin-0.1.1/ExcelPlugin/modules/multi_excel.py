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
        self.wb = Workbook()
        self.sheets: Dict[str, Excel] = {}
        self._remove_default_sheet()

    def _remove_default_sheet(self):
        if "Sheet" in self.wb.sheetnames:
            del self.wb["Sheet"]

    def __getitem__(self, key: str) -> Excel:
        return self.sheets[key]

    def add_sheet(
        self,
        data: pd.DataFrame,
        worksheet: str
    ) -> Excel:
        if worksheet in self.sheets:
            raise ValueError(f"Sheet '{worksheet}' already exists")

        sheet = Excel(
            data=data,
            workbook=self.wb,
            worksheet=worksheet
        )
        self.sheets[worksheet] = sheet
        return sheet

    def save(self, filename: str, filepath: Union[str, None]=None):
        for sheet in self.sheets.values():
            sheet._write_data()
        if filepath:
            self.wb.save(Path(filepath) / filename)
        else:
            self.wb.save(CURRENT_DIR / filename)
