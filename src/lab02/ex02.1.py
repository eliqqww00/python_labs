def transpose(mat):
    if mat == []:
        return []
    for i in mat:
        if len(i)!=len(mat[0]):
            raise ValueError
    res=[]
    for j in range(len(mat[0])): #колво столбцов = длина первой строки
        row=[]
        for i in range(len(mat)): #колво строк
            row.append(mat[i][j])
        res.append(row)
    return res

print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
# print(transpose([[1, 2], [3]]))