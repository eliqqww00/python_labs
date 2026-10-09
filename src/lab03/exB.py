from sys import *
from re import *
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    '''
    Нормализует текст: 
    приводит символы к нижнему регистру, 
    заменяет букву ё на е и убирает лишние пробелы. 

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
    
    :return: список найденных слов и чисел 
    '''

    p=r'[a-zA-Zа-яА-Я0-9_]+(?:-[a-zA-Zа-яА-Я0-9_]+)*'
    res=findall(p,text)
    return res

def count_freq(tokens: list[str]) -> dict[str, int]:

    ''' 
    Подсчитывает количество повторений каждого слова. 

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

    :return: список кортежей (слово, количество повторений)
    '''

    res=freq.items()  # получаем список вида (значение + колво)
    qq=sorted(res,key=lambda w: (-w[1],w[0]))
    return qq[:n]


text=stdin.read()
norm_text=normalize(text)
tokens=tokenize(norm_text)
pairs=count_freq(tokens)
top5=top_n(pairs)

print(f'''
Всего слов: {len(tokens)}
Уникальных слов: {len(set(tokens))}
Топ 5: ''')
for world,count in top5:
    print(f"{world}:{count}")