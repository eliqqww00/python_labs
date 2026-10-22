import json, csv
from pathlib import Path
from src.lib.functools import ensure_parent_dir

def json_to_csv(json_path: str, csv_path: str) -> None:
    '''Записывает значения

    Args:
        json_path: Путь к json файлу из которого читаем
        csv_path: Путь к csv файлу куда пишем

    Returns: 
        None

    Raises:
        FileNotFoundError: 
            Указанный JSON файл не найден
        ValueError:
            Указанный файл не формата JSON
            Пустой JSON или неподдерживаемая структура
            Файл JSON пустой или имеет неправильный формат
            Все элементы списка JSON должны быть словарями
    '''
    jp= Path(json_path)
    cp= Path(csv_path)

    #ошибки
    if not jp.exists():
        raise FileNotFoundError("файл не найден")
    
    if jp.suffix.lower() != ".json":
        raise ValueError("указанный файл не формата json")
    
    with jp.open(encoding="utf-8") as f:
        try:
            data = json.load(f)   #json -> python. загрузили в f
        except json.JSONDecodeError:
            raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not isinstance(data, list) or len(data) == 0:  #если НЕ список или пустой -> ошибка
        raise ValueError('Файл JSON пустой или имеет неправильный формат')
    
    if not all(isinstance(item, dict) for item in data):
        raise ValueError('Все элементы списка JSON должны быть словарями')

    names=[]
    for item in data:
        for key in item:
            if key not in names:
                names.append(key)
    
    ensure_parent_dir(cp)
    with cp.open("w",encoding="utf-8",newline="") as f:
        w= csv.DictWriter(f,fieldnames=names) #создали писателя, (куда писать,колонки)
        w.writeheader() #пишет первую строку, берет из списка names
        w.writerows(data) #пишет строки и автоматически раскидывает их по колонкам



def csv_to_json(csv_path: str, json_path: str) -> None:
    '''Записывает значения

    Args:
        csv_path: Путь к csv файлу из которого читаем
        json_path: Путь к json файлу куда пишем

    Returns: 
        None

    Raises:
        FileNotFoundError: 
            Указанный CSV файл не найден
        ValueError:
            Указанный файл не формата CSV
            Файл CSV пустой
            Файл CSV не содержит данных
    '''
    jp=Path(json_path)
    cp=Path(csv_path)

    #ошибки
    if not cp.exists():
        raise FileNotFoundError("Указанный CSV файл не найден")
    if cp.suffix.lower() != '.csv':
        raise ValueError("Указанный файл не формата CSV")
    with cp.open("r",encoding='utf-8',newline='') as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:  #заголовки отсуствуют
            raise ValueError("Файл CSV пустой")

        data = list(reader)  #список словарей
    if not data:
        raise ValueError("Файл CSV не содержит данных")

    ensure_parent_dir(jp)
    with jp.open('w',encoding='utf-8') as p:
        json.dump(data, p, ensure_ascii=False, indent=2) #python -> json,
        # (что записываем, открытый файл\куда пишем, настройки)

if __name__ == '__main__':
    json_to_csv("data/lab05/samples/people.json","data/lab05/out/people_from_json")
    csv_to_json("data/lab05/samples/people.csv","data/lab05/out/people_from_src")