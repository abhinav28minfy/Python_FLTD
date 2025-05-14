def transform_grades(grades):
    nd={}
    for i in grades:
        nd[i]={"average": sum(grades[i])/len(grades[i]), "highest": max(grades[i]), "lowest": min(grades[i])}
    return nd


grades = {
    "Alice": [85, 90, 95],
    "Bob": [70, 80, 90],
    "Charlie": [90, 92, 93]
}

print(transform_grades(grades))