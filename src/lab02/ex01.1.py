def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    ''' Вычисляет максимум и минимум списка

    Args: 
        nums: Список чисел (целых и вещественных)

    Returns:
        Кортеж (минимум, максимум)

    Raises:
        ValueError: Если список пустой
    '''
    if len(nums)==0: 
        raise ValueError ('пустой список')
    minimum=nums[0]
    maximim=nums[0]
    for i in nums:
        if i<minimum:
            minimum=i
        if i>maximim:
            maximim=i
    return (minimum,maximim)

print(f'''
тест кейсы:

[3, -1, 5, 5, 0] -> {min_max([3, -1, 5, 5, 0])}
[42] -> {min_max([42])}
[-5, -2, -9] -> {min_max([-5, -2, -9])}
[1.5, 2, 2.0, -3.1] -> {min_max([1.5, 2, 2.0, -3.1])}
''')
# Тест кейс который выводит ошибку ValueError
# print(f'[] -> {min_max([])}')
