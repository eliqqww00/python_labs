def transpose(mat: list[list[float | int]]) -> list[list]:

    '''Меняет строки и столбцы местами

    Args:
        mat: Матрица

    Returns:
        trans: Транспонированная матрица

    Raises:
        ValueError: Строки разной длины
    '''

    if mat == []:
        return []
    for i in mat:
        if len(i)!=len(mat[0]):
            raise ValueError ('Строки разной длины')
    res=[]
    for j in range(len(mat[0])): #колво столбцов = длина первой строки
        row=[]
        for i in range(len(mat)): #колво строк
            row.append(mat[i][j])
        res.append(row)
    return res

print(f'''
тест кейсы / transpose
[[1, 2, 3]] -> {transpose([[1, 2, 3]])}
[[1], [2], [3]] -> {transpose([[1], [2], [3]])}
[[1, 2], [3, 4]] -> {transpose([[1, 2], [3, 4]])}
[] -> {transpose([])}
''')

# Возвращает ошибку ValueError
# print(f'[[1, 2], [3]] -> {transpose([[1, 2], [3]])}')
