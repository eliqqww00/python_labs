from src.lab08.models import student_to_dict, student_from_dict
from pathlib import Path
from src.lab04.io_txt_csv import read_text
import json

def students_to_json(students, path) -> None:
    '''Сохраняет список записей студентов в JSON-файл с предварительной валидацией.'''
    jp=Path(path)
    data = [student_to_dict(s) for s in students]
    with jp.open('w',encoding='utf-8') as p:
        json.dump(data, p, ensure_ascii=False, indent=2)
    
def students_from_json(path) -> list[dict]:
    '''Загружает список студентов из JSON со строгой валидацией каждой записи.

    Политика обработки битых записей: strict. Первая битая запись
    вызывает ValueError с номером записи и причиной.
    '''

    text = read_text(path)
    if not text.strip():
        raise ValueError(f'файл {path} пуст')
        
    jp=Path(path)
    try:
        with jp.open('r',encoding='utf-8') as p:
            data=json.load(p)
    except json.JSONDecodeError as e:
        raise ValueError(f"Некорректный формат JSON в файле {path}: {e}") from e

    if not isinstance(data,list):
        raise ValueError (f'ожидался json-массив, получено {type(data)}')

    students=[]
    for i,item in enumerate(data,1):
        try:
            students.append(student_from_dict(item))
        except ValueError as e:
            raise ValueError (f'ошибка в записи под indx {i}: {e}') from e
    return students

if __name__ == '__main__':
    input_file = 'data/lab08/students_input.json'
    output_file = 'data/lab08/students_output.json'
    bad_file = 'data/lab08/students_bad.json'

    # 1. туда и обратно
    print (f'чтение из {input_file}, сохранение в {output_file}')
    try:
        students_list = students_from_json(input_file)

        students_to_json(students_list,output_file)
    except ValueError as e:
        print(f'ошибка: {e}')

    # 2. битый
    try:
        students_from_json('data/lab08/students_bad.json')
    except ValueError as e:
        print(f'ошибка: {e}')