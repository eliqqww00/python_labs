def min_max(nums):
    if len(nums)==0: raise ValueError
    minimum=nums[0]
    maximim=nums[0]
    for i in nums:
        if i<minimum:
            minimum=i
        if i>maximim:
            maximim=i
    return (minimum,maximim)

print(min_max([3, -1, 5, 5, 0]))