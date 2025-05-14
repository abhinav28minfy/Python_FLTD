def invert_dict(d):
    nd={}
    for i in d:
        nd[d[i]]=i
    return nd

print(invert_dict({"car":"Toyota", "truck":"Ford", "van":"Honda"}))