def flatten(mat: list[list | tuple]) -> list:

    '''Переводит матрицу в вектор

    Args:
        mat: Список в котором содержатся списки или кортежи
    
    Returns:
        vector: Список
    
    Raises:
        TypeError: Если передана не матрица
    '''

    vector=[]
    for i in mat:
        if type(i)!=list and type(i)!=tuple:
            raise TypeError("Передана не матрица")
        vector.extend(i)
    return vector

print(f'''
тест кейсы / flatten
[[1, 2], [3, 4]] -> {flatten([[1, 2], [3, 4]])}
[[1, 2], (3, 4, 5)] -> {flatten([[1, 2], (3, 4, 5)])}
[[1], [], [2, 3]] -> {flatten([[1], [], [2, 3]])}
''')

# Тест кейс который выводит ошибку TypeError
# print(f'[[1, 2], "ab"] -> {flatten([[1, 2], "ab"])}') 