def row_sums(mat: list[list[float | int]]) -> list[float]:

    '''Сумма по каждой строке

    Args: 
        mat: Матрица чисел

    Returns:
        Список сумм по строке

    Raises:
        ValueError: Строки разной длины
    '''
    if len(mat)==0:
        return []
    res=[]
    for i in mat:
        if len(i)!=len(mat[0]):
            raise ValueError ('Строки разной длины')
    for i in range(len(mat)):
        res.append(sum(mat[i]))
    return res

print(f'''
тест кейсы / row_sums
[[1, 2, 3], [4, 5, 6]] -> {row_sums([[1, 2, 3], [4, 5, 6]])}
[[-1, 1], [10, -10]] -> {row_sums([[-1, 1], [10, -10]])}
[[0, 0], [0, 0]] -> {row_sums([[0, 0], [0, 0]])}
''')
# Возвращает ошибку ValueError
# print(f'[[1, 2], [3]] -> {row_sums([[1, 2], [3]])}')