from sys import *
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

text=stdin.read()
text=normalize(text)
n=len(text)
k=len(set(text))
freq=tokenize(text)
pairs=count_freq(freq)
print(pairs)
top=top_n(pairs)
for world,count in top:
    print(f"{world}:{count}")