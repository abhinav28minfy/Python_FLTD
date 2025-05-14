def count_coordinate_occurances(coords):
    d={}
    for coord in coords:
        if coord in d:
            d[coord] += 1
        else:
            d[coord] = 1
    return d

coords = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
print(count_coordinate_occurances(coords))