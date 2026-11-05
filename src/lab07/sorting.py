def bubble_sort(nums):
    ln = len(nums)
    result=nums[:]
    for i in range(0,ln):
        for j in range(0,ln-i-1):
            if result[j] > result[j+1]:
                result[j],result[j+1] = result[j+1],result[j]
    return result
 
def insertion_sort(nums):
    result = nums[:]
    for i in range(1,len(result)):
        key=result[i] #число, которое вставляем
        j=i-1 #левый сосед
        while j>=0 and result[j]>key:
            result[j+1] = result[j] #сдвигаем соседа
            j-=1 #идем дальше влево
        result[j+1]=key #ставим число на найденное место
    return result
 
 
def selection_sort(nums):
    result=nums[:]
    ln=len(nums)
    for i in range(0,ln):
        min_indx = i  #пока считаем минимумом число на позиции i
        for j in range(i+1,ln):  #смотрим всех правее
            if result[j] < result[min_indx]:  #нашли меньше
                min_indx = j  #запомнили, где оно лежит
        result[i],result[min_indx]=result[min_indx],result[i]  #поставили минимум на место i
    return result