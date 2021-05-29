def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])

    return parent[a]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b


V, E = map(int, input().split())
arr = []
parent = [0] * (V + 1)
total = 0

for i in range(1, V + 1):
    parent[i] = i

for i in range(E):
    a, b, c = map(int, input().split())
    arr.append((a, b, c))

arr = sorted(arr, key=lambda x: x[2])

for i in range(E):

    a, b, c = arr[i]

    a = find_parent(a)
    b = find_parent(b)

    if a != b:
        union(a, b)
        total += c

print(total)
