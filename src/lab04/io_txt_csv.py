import csv
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''Считывает текст по указанному пути

    Args:
        path: Путь к файлу в формате строки или Path
        encoding: Тип кодировки файла (пример: encoding="cp1251"), по умолчанию utf-8

    Returns:
        Содержимое файла в виде строки

    Raises:
        FileNotFoundError: файл не найден.
        UnicodeDecodeError: кодировка не подходит для этого файла.
    '''
    with open(path, "r", encoding=encoding) as f:
        return f.read()


def ensure_parent_dir(path: str | Path) -> None:
    '''Проверяет наличие родительских папок, если их нет, то создает их
    Args:
        path: Путь к файлу в формате строки или Path

    Returns:
        None
    '''
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def write_csv(rows: list[tuple | list], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    '''Записывает строки в CSV-файл

    Args:
        rows: Список строк (кортежи или списки одинаковой длины)
        path: Путь к файлу записи
        header: Заголовок, записывается первой строкой, если передан

    Raises:
        ValueError: строки разной длины
    '''
    p = Path(path)
    rows = list(rows)

    if rows:
        etalon = len(rows[0])
        for r in rows:
            if len(r) != etalon:
                raise ValueError('Строки разной длины')

    ensure_parent_dir(p)
    with p.open('w', newline="", encoding="utf-8") as f:
        w = csv.writer(f) #создаем писателя csv
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


#мини тесты
print(read_text("data/lab04/input.txt")) # должен вернуть строку
write_csv([("word","count"),("test",3)], "data/lab04/check.csv")  # создаст CSV

#краевые случаи для А
# 1. пустой файл
print(read_text("data/lab04/empty,a.txt"))
# 2. пустой rows без header -> пустой файл
write_csv([], "data/lab04/empty,a.csv")
# 3. пустой rows с header -> только заголовок
write_csv([], "data/lab04/header_only,a.csv", header=("a", "b"))
# 4. строки разной длины -> ValueError
write_csv([("a", 1), ("b",)], "data/lab04/bad,a.csv")