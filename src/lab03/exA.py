from re import *
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    if casefold:
        text=text.casefold()
    else:
        text=text.lower()

    if yo2e==True:
        text=text.replace('ё','е')

    text=' '.join(text.split())
    return text


def tokenize(text: str) -> list[str]:
    p=r'[a-zA-Zа-яА-Я0-9_]+(?:-[a-zA-Zа-яА-Я0-9_]+)*'
    res=findall(p,text)
    return res

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for w in tokens:
        freq[w]=freq.get(w,0)+1 #запрашиваем значение по ключу w из res, если значения нет -0
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    res=freq.items()  # получаем список вида (значение + колво)
    qq=sorted(res,key=lambda w: (-w[1],w[0]))
    return qq[:n]
