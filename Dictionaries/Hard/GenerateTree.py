def generate_tree(paths):
    tree={}
    for path in paths:
        parts=path.split('/')
        current=tree
        for part in parts:
            if part not in current:
                current[part]={}
            current=current[part]
    return tree

paths=[
    "folder1/file1.txt",
    "folder1/folder2/file2.txt",
    "folder3/file3.txt"
]

print(generate_tree(paths))