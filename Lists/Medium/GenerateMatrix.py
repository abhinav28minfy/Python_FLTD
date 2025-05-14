def generate_matrix(n,m):
    matrix=[]
    for i in range(n):
        row=[]
        for j in range(m):
            row.append(i*j)
        matrix.append(row)
    return matrix

print(generate_matrix(3,3))