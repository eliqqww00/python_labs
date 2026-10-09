from re import *
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    '''
    Нормализует текст: 
    приводит символы к нижнему регистру, 
    заменяет букву ё на е и убирает лишние пробелы. 

    :param text: исходный текст 
    :param casefold: использовать casefold() вместо lower() 
    :param yo2e: заменить ё на е 
    :return: нормализованный текст 
    '''

    if casefold:
        text=text.casefold()
    else:
        text=text.lower()

    if yo2e==True:
        text=text.replace('ё','е')

    text=' '.join(text.split())
    return text


def tokenize(text: str) -> list[str]:

    '''
    Разделяет текст на отдельные слова и числа. 
    Слова могут содержать символы подчёркивания и дефисы. 
    
    :param text: исходный текст 
    :return: список найденных слов и чисел 
    '''

    p=r'[a-zA-Zа-яА-Я0-9_]+(?:-[a-zA-Zа-яА-Я0-9_]+)*'
    res=findall(p,text)
    return res

def count_freq(tokens: list[str]) -> dict[str, int]:

    ''' 
    Подсчитывает количество повторений каждого слова. 
    :param tokens: список слов :
    :return: словарь, где ключ — слово, значение — количество его повторений 
    '''

    freq = {}
    for w in tokens:
        freq[w]=freq.get(w,0)+1 #запрашиваем значение по ключу w из res, если значения нет -0
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:

    '''
    Возвращает n самых часто встречающихся слов.

    Сначала слова сортируются по количеству повторений 
    от большего к меньшему, а при одинаковом количестве — по алфавиту. 

    :param freq: словарь со словами и количеством их повторений.
    :param n: количество слов, которые нужно вернуть 
    :return: список кортежей (слово, количество повторений)
    '''

    res=freq.items()  # получаем список вида (значение + колво)
    qq=sorted(res,key=lambda w: (-w[1],w[0]))
    return qq[:n]

print (f'''
тест кейсы / normalize

"ПрИвЕт\nМИр\t" -> {normalize("ПрИвЕт\nМИр\t")}
"ёжик, Ёлка" -> {normalize("ёжик, Ёлка")}
"Hello\r\nWorld" -> {normalize("Hello\r\nWorld")}
"  двойные   пробелы  " -> {normalize("  двойные   пробелы  ")}
''')

print (f'''
тест кейсы / tokenize

"привет мир" -> {tokenize("привет мир")}
"hello,world!!!" -> {tokenize("hello,world!!!")}
"по-настоящему круто" -> {tokenize("по-настоящему круто")}
"2025 год" -> {tokenize("2025 год")}
"emoji 😀 не слово" -> {tokenize("emoji 😀 не слово")}
''')

print (f'''
тест кейсы / count_freq + top_n

Токены ["a","b","a","c","b","a"] -> частоты {count_freq(["a","b","a","c","b","a"])}
top_n(..., n=2) -> {top_n({'a': 3, 'b': 2, 'c': 1},2)}
При равенстве частот: токены ["bb","aa","bb","aa","cc"] → частоты {count_freq(["bb","aa","bb","aa","cc"])}
top_n(..., n=2) → {top_n({'bb': 2, 'aa': 2, 'cc': 1},2)} (алфавитная сортировка при равенстве).
''')