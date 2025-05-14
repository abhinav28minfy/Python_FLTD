def filter_even_numbers(list):
    a=[]
    for i in list:
        if i%2==0:
            a.append(i)
    return a

l=[1,2,3,4,5,6,7,8,9]
print(filter_even_numbers(l))
