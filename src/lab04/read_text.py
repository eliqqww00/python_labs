import csv
from pathlib import Path
from typing import Iterable, Sequence
import sys 

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    try:
        with open(path, "r", encoding=encoding) as f:
            return f.read()
    except FileNotFoundError:
        print(f"файл не найден: {path}", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"кодировка не подходит: {encoding}", file=sys.stderr)
        sys.exit(1)
print(read_text())

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)