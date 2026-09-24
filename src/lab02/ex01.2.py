def unique_sorted(nums: list[float | int]) -> list[float | int]:

    '''Возвращает отсортированный список

    Args:
        nums: Список чисел (целых и вещественных)

    Returns:
        Отсортированный список
    '''

    for i in nums:
        if nums.count(i)>1:
            while nums.count(i)>1:
                nums.remove(i)
    res=[]
    while nums:
        minimum=nums[0]
        for i in nums:
            if i<minimum:
                minimum=i
        nums.remove(minimum)
        res.append(minimum)
    return res

print(f'''
тест кейсы / unique_sorted
[3, 1, 2, 1, 3] -> {unique_sorted([3, 1, 2, 1, 3])}
[] -> {unique_sorted([])}
[-1, -1, 0, 2, 2] -> {unique_sorted([-1, -1, 0, 2, 2])}
[1.0, 1, 2.5, 2.5, 0] -> {unique_sorted([1.0, 1, 2.5, 2.5, 0])}
''')