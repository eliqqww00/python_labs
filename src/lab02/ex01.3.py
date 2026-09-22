def flatten(mat):
    vector=[]
    for i in mat:
        if type(i)!=list and type(i)!=tuple:
            raise TypeError("Передана не матрица")
        vector.extend(i)
    return vector
print(flatten([[1, 2], [3, 4]]))