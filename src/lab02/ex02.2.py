def row_sums(mat):
    res=[]
    for i in mat:
        if len(i)!=len(mat[0]):
            raise ValueError 
    for i in range(len(mat)):
        res.append(sum(mat[i]))
    return res

print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
# print(row_sums([[1, 2], [3]]))