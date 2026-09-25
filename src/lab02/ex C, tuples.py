def format_record(rec: tuple[str, str, float]) -> str:
    
    '''Функция форматирует запись, приводя ее в вид 
    Иванов И.И., гр. BIVT-25, GPA 4.60

    Args:
        rec: Кортеж в котором содержится ФИО, группа и оценка

    Returns:
        Строку, где указано имя, инициалы, группа и оценка

    Raises:
        TypeError:
            'Запись должна быть кортежем'
            'Имя должно быть строкой'
            'Группа должна быть строкой'
            'Оценка должна быть вещественным числом'
            'GPA должен быть от 0.0 до 5.0'
        ValueError:
            'В кортеже должно быть 3 элемента'
            'Введено не полное ФИО'
            'Группа не может быть пустой'
    '''

    #ошибки
    if not isinstance(rec, tuple):
        raise TypeError('Запись должна быть кортежем')
    if len(rec) != 3:
        raise ValueError('В кортеже должно быть 3 элемента')
    if not isinstance(rec[0], str):
        raise TypeError('Имя должно быть строкой')
    if not isinstance(rec[1], str):
        raise TypeError('Группа должна быть строкой')
    if not isinstance(rec[2], (float, int)):
        raise TypeError('Оценка должна быть вещественным числом')
    if rec[2] < 0.0 or rec[2] > 5.0:
        raise ValueError('GPA должен быть от 0.0 до 5.0')
    if len(rec[0].strip().split()) != 3 and len(rec[0].strip().split()) != 2:
        raise ValueError('Введено не полное ФИО')
    if len(rec[1].strip())==0:
        raise ValueError('Группа не может быть пустой')

    fio_parts=rec[0].strip().split()
    name=fio_parts[1]
    surname=fio_parts[0].capitalize()
    group=rec[1]
    gpa=rec[2]
    if len(fio_parts)==3:
        initials=surname+' '+name[0].upper()+'.'+fio_parts[2][0].upper()+'.'
    elif len(fio_parts)==2:
        initials=surname+' '+name[0].upper()+'.'
    return (f"{initials}, гр. {group}, GPA {gpa:.2f}")

#выводы
print(f'''
тест кейсы / tuples
("Иванов Иван Иванович", "BIVT-25", 4.6) -> {format_record(("Иванов Иван Иванович", "BIVT-25", 4.6))}
("Петров Пётр", "IKBO-12", 5.0) -> {format_record(("Петров Пётр", "IKBO-12", 5.0))}
("Петров Пётр Петрович", "IKBO-12", 5.0) -> {format_record(("Петров Пётр Петрович", "IKBO-12", 5.0))}
("  сидорова  анна   сергеевна ", "ABB-01", 3.999) -> {format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))}
''')
#Возвращает ошибку TypeError
#print(f'("Иванов Иван", "BIVT-25", 5.1) -> {format_record(("Иванов Иван", "BIVT-25", 5.1))}')