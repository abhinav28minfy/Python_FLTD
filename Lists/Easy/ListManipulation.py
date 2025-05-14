def merge_sorted_lists(l1,l2):
    l3=[]
    i=0
    j=0
    while len(l1)>i and len(l2)>j:
        if(l1[i]>=l2[j]):
            l3.append(l2[j])
            j+=1
        else:
            l3.append(l1[i])
            i+=1
    
    while i<len(l1):
        l3.append(l1[i])
        i+=1
    while j<len(l2):
        l3.append(l2[j])
        j+=1

    return l3


print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))