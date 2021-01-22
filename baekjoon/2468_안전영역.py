from copy import deepcopy
from collections import deque


def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    flag = 0

    while queue:

        a, b = queue.popleft()
        if arr_copy[a][b] != 0:
            arr_copy[a][b] = 0
            flag = 1

            for i in range(4):
                dx = a + nx[i]
                dy = b + ny[i]

                if dx < 0 or dx >= N or dy < 0 or dy >= N:
                    continue

                queue.append((dx, dy))

    if flag == 1:
        return True

    return False


N = int(input())
arr = []
poc = []
M = 1
m = 100
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]
ct = 0

for i in range(N):
    arr.append(list(map(int, input().split())))

for i in range(0, 101):
    arr_copy = deepcopy(arr)
    for j in range(N):
        for z in range(N):
            if arr_copy[j][z] <= i:
                arr_copy[j][z] = 0

    for j in range(N):
        for z in range(N):
            if BFS(j, z) == True:
                ct += 1

    poc.append(ct)
    ct = 0

print(max(poc))