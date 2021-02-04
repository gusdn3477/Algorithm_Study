import sys

sys.setrecursionlimit(100000)


def DFS(x, y):
    arr[x][y] = '0'

    for i in range(8):
        dx = x + nx[i]
        dy = y + ny[i]

        if dx < 0 or dx >= N or dy < 0 or dy >= M:
            continue

        if arr[dx][dy] == '1':
            DFS(dx, dy)


N, M = map(int, input().split())
arr = []
ct = 0
nx = [-1, -1, -1, 0, 1, 1, 1, 0]
ny = [-1, 0, 1, 1, 1, 0, -1, -1]

for i in range(N):
    arr.append(list(input().split()))

for i in range(N):
    for j in range(M):
        if arr[i][j] == '1':
            DFS(i, j)
            ct += 1

print(ct)