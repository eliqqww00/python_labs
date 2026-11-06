import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_to_xlsx import csv_to_xlsx
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="command")

    p1 = sub.add_parser("json2csv", help='Конвертировать JSON в CSV')
    p1.add_argument("--in", dest="input", required=True, help="Входной файл JSON")
    p1.add_argument("--out", dest="output", required=True, help="Выходной файл CSV")

    p2 = sub.add_parser("csv2json", help='Конвертировать CSV в JSON')
    p2.add_argument("--in", dest="input", required=True, help="Входной файл CSV")
    p2.add_argument("--out", dest="output", required=True, help="Выходной файл JSON")

    p3 = sub.add_parser("csv2xlsx", help='Конвертировать CSV в XLSX')
    p3.add_argument("--in", dest="input", required=True, help="Входной файл CSV")
    p3.add_argument("--out", dest="output", required=True, help="Выходной файл XLSX")

    args = parser.parse_args()

    if args.command is None:
        parser.error("Нужно указать подкоманду: json2csv, csv2json или csv2xlsx")

    try:
        if args.command == "json2csv":
            json_to_csv(Path(args.input),Path(args.output))

        elif args.command == "csv2json":
            csv_to_json(Path(args.input),Path(args.output))

        elif args.command == "csv2xlsx":
            csv_to_xlsx(Path(args.input),Path(args.output))

    except FileNotFoundError:
        parser.error(f'Файл не найден: {args.input}')
    except UnicodeDecodeError:
        parser.error(f'Файл {args.input} написан в кодировке, отличной от UTF-8')
    except ValueError as error:
        parser.error(str(error))

if __name__ == "__main__":
    main()

# python -m src.lab06.cli_convert json2csv --in data/lab05/samples/people.json --out data/lab06/out/people.csv
# python -m src.lab06.cli_convert csv2json --in data/lab05/samples/people.csv --out data/lab06/out/people.json
# python -m src.lab06.cli_convert csv2xlsx --in data/lab05/samples/cities.csv --out data/lab06/out/cities.xlsx