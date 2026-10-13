def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError('Пустой список')
    minimum = nums[0]
    maximum = nums[0]
    for i in nums:
        if i < minimum:
            minimum = i
        if i > maximum:
            maximum = i
    return (minimum, maximum)



def unique_sorted(nums: list[float | int]) -> list[float | int]:
    nums = nums.copy()
    for i in nums:
        if nums.count(i) > 1:
            while nums.count(i) > 1:
                nums.remove(i)
    res = []
    while nums:
        minimum = nums[0]
        for i in nums:
            if i < minimum:
                minimum = i
        nums.remove(minimum)
        res.append(minimum)
    return res



def flatten(mat: list[list | tuple]) -> list:
    vector = []
    for i in mat:
        if type(i) != list and type(i) != tuple:
            raise TypeError('Передана не матрица')
        vector.extend(i)
    return vector



def transpose(mat: list[list[float | int]]) -> list[list]:
    if mat == []:
        return []
    for i in mat:
        if len(i) != len(mat[0]):
            raise ValueError('Строки разной длины')
    res = []
    for j in range(len(mat[0])):
        row = []
        for i in range(len(mat)):
            row.append(mat[i][j])
        res.append(row)
    return res



def row_sums(mat: list[list[float | int]]) -> list[float]:
    res = []
    for i in mat:
        if len(i) != len(mat[0]):
            raise ValueError('Строки разной длины')
    for i in range(len(mat)):
        res.append(sum(mat[i]))
    return res



def col_sums(mat: list[list[float | int]]) -> list[float]:
    for row in mat:
        if len(row) != len(mat[0]):
            raise ValueError('Строки разной длины')
    res = []
    for j in range(len(mat[0])):
        s = 0
        for i in range(len(mat)):
            s += mat[i][j]
        res.append(s)
    return res



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