def transpose_matrix(matrix):
    l=[]
    for i in range(len(matrix[0])):
        row=[]
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        l.append(row)
    return l

matrix=[[1,2,3],[4,5,6]]
print(transpose_matrix(matrix))
