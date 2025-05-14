def swap_pairs(t):
    swapped=[]
    i=0
    while i<len(t)-1:
        swapped.append(t[i+1])
        swapped.append(t[i])
        i+=2
    if(len(t)%2!=0):
        swapped.append(t[-1])
    return swapped

print(swap_pairs((1,2,3,4,5)))