def col_sums(mat):
    for row in mat:
            if len(row) != len(mat[0]):
                raise ValueError
    res=[]
    for j in range(len(mat[0])):
        s=0
        for i in range(len(mat)):
            s+=mat[i][j]
        res.append(s)
    return res

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
# print([[1, 2], [3]])