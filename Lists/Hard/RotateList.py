def rotate_list(l,k):
    n=len(l)
    k=k%n

    rotated=[]
    for i in range(n-k,n):
        rotated.append(l[i])
    for i in range(0,n-k):
        rotated.append(l[i])
    
    return rotated

print(rotate_list([1, 2, 3, 4, 5], 2))

