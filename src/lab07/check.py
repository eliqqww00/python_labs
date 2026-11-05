import random
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
 
 
def check_sorting(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums) #вызов моей сортировки
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"

def check_search(trials=100):
    count = 0
    for _ in range(trials):
        n=random.randint(0,50)
        nums = [random.randint(-20,20) for _ in range(n)]

        # --- линейный поиск ---
        linear_targets = [nums[0], nums[-1], random.randint(-20,20)]
        for x in linear_targets:
            try:
                expected = nums.index(x)
            except ValueError:
                expected = -1
            result = linear_search(nums,x)
            assert result == expected, f'linear_search ошиблась на {nums}, x={x}: {result}, ожидалось {expected}'
            count+=1

        # --- бинарный поиск ---
        sorted_nums=sorted(nums)
        binary_targets = [-5, 5, random.randint(-4,4)]
        if sorted_nums:
            binary_targets.append(sorted_nums[-1])
            binary_targets.append(sorted_nums[0])
            binary_targets.append(random.choise(sorted_nums))
        
        for x in binary_targets:
            result = binary_search(sorted_nums,x)
            # if x in sorted_nums:
            # else:
            #     assert -1, f'binary_search ошиблась на {sorted_nums}, x={x}'
    return count

def check_two_sum(trials=100):
    n = random.randint(0, 20)
    nums = [random.randint(-20, 20) for _ in range(n)]
    target = random.randint(-30, 30)
    a = two_sum_brute(nums, target)
    b = two_sum_fast(nums, target)
    assert (a is None) == (b is None), f"расходятся на {nums}, target={target}: brute={a}, fast={b}"
    assert a

 
if __name__ == "__main__":
    random.seed(42)
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
    # TODO: check_search(), check_two_sum()
    print("OK")