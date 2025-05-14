def find_peak(l):
    peak=[]
    l.append(0)
    l.insert(0,0)
    for i in range(1, len(l)-1):
        if l[i]>l[i-1] and l[i]>l[i+1]:
            peak.append(i-1)
    return peak

l=[1, 3, 2, 3, 5, 4, 3, 2, 3, 1]
print(find_peak(l))