import random
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
 
 
def check_sorting(fn, trials=100):
    count=0
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums) #вызов моей сортировки
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"
        count+=1
    return count

def check_search(trials=100):
    count = 0
    for _ in range(trials):
        n=random.randint(1,50)
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
        binary_targets = [-21, 21, random.randint(-20,20)]
        if sorted_nums:
            binary_targets.append(sorted_nums[-1])
            binary_targets.append(sorted_nums[0])
            binary_targets.append(random.choice(sorted_nums))
        
        for x in binary_targets:
            try:
                expected = sorted_nums.index(x)
            except ValueError:
                expected = -1
            result = binary_search(sorted_nums,x)
            if expected == -1:
                assert result == -1, f"binary_search ошиблась на {sorted_nums}, x={x}: {result}, ожидалось -1"
            else:
                assert result != -1, f"binary_search не нашла {x} в {sorted_nums}"
                assert sorted_nums[result] == x, f"binary_search вернула {result}, а там не {x}: {sorted_nums}"
                # ожидается, что условие истина, иначе выпадает пояснение
            count+=1
    return count

def check_two_sum(trials=100):
    count=0
    for _ in range(trials):
        n = random.randint(0, 20)
        nums = [random.randint(-20, 20) for _ in range(n)]
        target = random.randint(-30, 30)
        a = two_sum_brute(nums, target)
        b = two_sum_fast(nums, target)
        assert (a is None) == (b is None), f"расходятся на {nums}, target={target}: brute={a}, fast={b}"
        if a is not None:
            assert (nums[a[0]]+nums[a[1]])==target, f"расходятся на {nums}, target={target}: a1= {nums[a[0]],a[0]}, a2= {nums[a[1]],a[1]}"
        if b is not None:
            assert (nums[b[0]]+nums[b[1]])==target, f"расходятся на {nums}, target={target}: b1= {nums[b[0]],b[0]}, b2= {nums[b[1]],b[1]}"
        count+=1
    return count

 
if __name__ == "__main__":
    random.seed(42)
    N=0
    for fn in (bubble_sort, insertion_sort, selection_sort):
        N+=check_sorting(fn)
    N+=check_search()
    N+=check_two_sum()
    print(f"OK, {N} проверок")