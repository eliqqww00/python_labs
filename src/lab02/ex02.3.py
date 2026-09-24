def col_sums(mat: list[list[float | int]]) -> list[float]:

    '''Сумма по каждому столбцу

    Args:
        mat: Матрица чисел

    Returns:
        Список сумм по столбцам

    Raises:
        ValueError: Строки разной длины
    '''

    for row in mat:
            if len(row) != len(mat[0]):
                raise ValueError ('Строки разной длины')
    res=[]
    for j in range(len(mat[0])):
        s=0
        for i in range(len(mat)):
            s+=mat[i][j]
        res.append(s)
    return res

print(f'''
тест кейсы / col_sums
[[1, 2, 3], [4, 5, 6]] → {col_sums([[1, 2, 3], [4, 5, 6]])}
[[-1, 1], [10, -10]] → {col_sums([[-1, 1], [10, -10]])}
[[0, 0], [0, 0]] → {col_sums([[0, 0], [0, 0]])}
''')
# Возвращает ошибку ValueError
# print(f'[[1, 2], [3]] -> {col_sums([[1, 2], [3]])}')