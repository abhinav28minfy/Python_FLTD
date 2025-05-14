def flatten_tuple(t):
    result=()
    for item in t:
        if isinstance(item,tuple):
            # is instance helps identify the type of something
            result += flatten_tuple(item)
        else:
            result += (item,)
    return result

nested = (1, (2, 3), (4, (5, 6)), 7)
print(flatten_tuple(nested))