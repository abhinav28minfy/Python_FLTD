def merge_dict(d1,d2):
    for i in d2:
        d1[i]=d2[i]
    return d1

print(merge_dict({"car":"Toyota", "truck":"Ford", "van":"Honda"}, {"car":"Nissan", "truck":"Chevy"}))