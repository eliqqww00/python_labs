from openpyxl import Workbook
import csv
from pathlib import Path
from src.lib.functools import ensure_parent_dir

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    '''Конвертирует CSV файл в формат XLSX.

        Args:
            csv_path: Путь к исходному CSV файлу
            xlsx_path: Путь для сохранения XLSX файла

        Returns:
            None

        Raises:
            FileNotFoundError:
                Указанный CSV файл не найден
            ValueError:
                Указанный файл не формата CSV
                Файл CSV пустой
    '''
    cp=Path(csv_path)
    xlp=Path(xlsx_path)

    #ошибки
    if not cp.exists():
        raise FileNotFoundError("Указанный CSV файл не найден")
    if cp.suffix.lower() != ".csv":
        raise ValueError("Указанный файл не формата CSV")
    rows=[]
    with cp.open('r',encoding='utf-8',newline='') as f:
        rows=list(csv.reader(f))  #список списков
        #reader: каждая строка со значениями -> список значений
    if not rows:
        raise ValueError("Файл CSV пустой")


    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    for row in rows:
        ws.append(row)
    ensure_parent_dir(xlp)
    wb.save(xlp)

if __name__ == '__main__':
    csv_to_xlsx("data/lab05/samples/cities.csv","data/lab05/out/cities_from_csv.xlsx")