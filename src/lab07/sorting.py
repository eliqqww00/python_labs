def bubble_sort(nums):
    ''' Возвращает отсортированный список методом пузырьковой сортировки. 
    Исходный список не меняется. '''
    ln = len(nums)
    result=nums[:]
    for i in range(0,ln):
        for j in range(0,ln-i-1):
            if result[j] > result[j+1]:
                result[j],result[j+1] = result[j+1],result[j]
    return result

def insertion_sort(nums):
    ''' Возвращает отсортированный список методом сортировки вставками.
    Исходный список не меняется. '''
    result = nums[:]
    for i in range(1,len(result)):
        key=result[i]
        j=i-1
        while j>=0 and result[j]>key:
            result[j+1] = result[j]
            j-=1
        result[j+1]=key
    return result
 
 
def selection_sort(nums):
    ''' Возвращает отсортированный список методом сортировки выбором.
    Исходный список не меняется. '''
    result=nums[:]
    ln=len(nums)
    for i in range(0,ln):
        min_indx = i
        for j in range(i+1,ln):
            if result[j] < result[min_indx]:
                min_indx = j
        result[i],result[min_indx]=result[min_indx],result[i]
    return result