def get_stats(li):
    ma=max(li)
    mi=min(li)
    s=sum(li)
    avg=s/len(li)
    t=(mi,ma,avg,s)
    return t

print(get_stats([1,2,3,4,5]))