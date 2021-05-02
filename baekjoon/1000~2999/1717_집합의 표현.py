from sys import stdin, setrecursionlimit

setrecursionlimit(30000)


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])

    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b


N, M = map(int, stdin.readline().split())
parent = [0] * (N + 2)

for i in range(0, N + 2):
    parent[i] = i

for i in range(M):
    a, b, c = map(int, stdin.readline().split())

    if a == 0:
        union_parent(b, c)

    else:
        if find_parent(b) == find_parent(c):
            print('YES')

        else:
            print('NO')