parent = [0, 1, 1, 2]

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x
    
a = find_parent(parent, 3)
print(a)

