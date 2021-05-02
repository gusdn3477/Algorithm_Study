from sys import stdin


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])

    return parent[x]


def union_parent(a, b):
    a, b = find_parent(a), find_parent(b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b


N, M = map(int, stdin.readline().split())
parent = [0] * N
flag = 0

for i in range(N):
    parent[i] = i

for i in range(1, M + 1):

    a, b = map(int, stdin.readline().split())

    if find_parent(a) != find_parent(b):
        union_parent(a, b)

    else:
        flag = 1
        break

if flag == 1:
    print(i)

else:
    print(0)