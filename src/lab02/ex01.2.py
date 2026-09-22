def unique_sorted(nums):
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

print(unique_sorted([2, 3, 1, 1, 2, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))