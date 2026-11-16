from datetime import date

student_fields = ("fio", "birthdate", "group", "gpa")

# проверки каждого значения
def check_fio(value) -> None:
    if not isinstance(value,str):
        raise ValueError(f"fio: ожидается строка, получено {type(value)}")
    if not value.strip():
        raise ValueError('fio: не должно быть пустым')

def check_data(value) -> None:
    if not isinstance(value,str):
        raise ValueError(f"birthdate: ожидается строка, получено {type(value)}")
    if not value.strip():
        raise ValueError('birthdate: не должно быть пустым')
    
    try:
        born = date.fromisoformat(value)
    except ValueError:
        raise ValueError(f'birthdate: некорректная дата {value}, требуется формат YYYY-MM-DD')
    if born > date.today():
        raise ValueError(f'{value} дата из будущего, студент еще не родился')

def check_group(value) -> None:
    if not isinstance(value,str):
        raise ValueError(f"group: ожидается строка, получено {type(value)}")
    if not value.strip():
        raise ValueError('group: не должно быть пустым')

def check_gpa(value) -> None:
    if isinstance(value,bool) or not isinstance(value,(int,float)):
        raise ValueError(f"gpa: ожидается число, получено {type(value)}")
    if not (0 <= value <= 5):
        raise ValueError(f"gpa: значение {value} вне диапазона [0,5]")


def make_student(fio, birthdate, group, gpa) -> dict:
    '''Собрать запись студента, проверив каждое значение'''
    check_fio(fio)
    check_data(birthdate)
    check_group(group)
    check_gpa(gpa)

    return {
        'fio': fio.strip(),
        'birthdate': birthdate,
        'group': group.strip(),
        'gpa': float(gpa),
    }

def validate_student(rec) -> None:
    '''Проверить итоговую запись, при ошибке ValueError'''
    if not isinstance(rec, dict):
        raise ValueError(f'ожидается словарь, получено {type(rec)}')
    
    expected = set(student_fields) #ожидаемые ключи
    actual = set(rec) # полученные ключи
    if actual != expected:
        missing = expected - actual
        extra = actual - expected
        raise ValueError(f'неверный набор ключей: не хватает {missing}, лишние {extra}')
    
    check_fio(rec['fio'])
    check_data(rec['birthdate'])
    check_group(rec['group'])
    check_gpa(rec['gpa'])

def student_age(rec, today=None) -> int:
    '''Вычисляет полных лет студента на дату today (по умолчанию сегодня).'''
    if today == None:
        today = date.today()
    born = date.fromisoformat(rec['birthdate'])
    had_birthday = (today.month, today.day) >= (born.month, born.day)
    if had_birthday == True:
        return today.year - born.year
    else:
        return today.year - born.year - 1

def format_student(rec) -> str:
    '''Форматирует запись студента в читаемую строку с инициалами и возрастом.'''
    parts = rec['fio'].split()
    second_name = parts[0]
    initials = ''.join(p[0].upper() + '.' for p in parts[1:])
    group = rec['group']
    age = student_age(rec)
    gpa = f"{rec['gpa']:.2f}"
    return f"{second_name} {initials} ({group}), {age} лет, GPA {gpa}"

def student_to_dict(rec) -> dict:
    '''Копия записи (новый словарь) для сериализации.'''
    return dict(rec)

def student_from_dict(d) -> dict:
    '''Десериализация: ровно нужные ключи, gpa -> float, валидация.'''
    if not isinstance(d,dict):
        raise ValueError(f'ожидается dict, получен {type(d)}')

    missing = [k for k in student_fields if k not in d]
    if missing:
        raise ValueError(f'отсутствуют ключи: {missing}')

    rec = {k: d[k] for k in student_fields} #собираем словарь с нужными ключами
    #автоматически избавляемся от лишних ключей

    gpa=rec['gpa']
    if isinstance(gpa,bool):
        raise ValueError('gpa: bool не допускается')
    try:
        rec['gpa'] = float(gpa)
    except (TypeError, ValueError):
        raise ValueError(f'gpa: не удалось привести {gpa} к float')

    validate_student(rec)

    return rec

if __name__ == '__main__':
    # 1. создание корректного студента
    student = make_student('Родионова Елизавета Андреевна', '2009-04-22', 'БИВТ-26-6-2', 4)
    print('Создан студент:', student)

    # 2. Форматирование
    print('Форматирование:', format_student(student))

    # 3. Ошибка
    print('Попытка создать студента с gpa=7')
    try:
        make_student('Иванов Иван Иванович', '2007-09-02', 'БПМ-25-5-1', 7)
    except ValueError as e:
        print('Перехвачена ошибка', e)

    # 4. Проверка даты рождения
    age = student_age(student) #today: 2026-11-16
    print('Возраст студента:', age)
