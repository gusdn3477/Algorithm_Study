import sys

sys.setrecursionlimit(10000)


def DFS(x, y):
    visited[x][y] = 1

    for i in range(4):

        dx = x + nx[i]
        dy = y + ny[i]

        if dx < 0 or dx >= N or dy < 0 or dy >= M:
            continue

        if visited[dx][dy] == 0 and arr[dx][dy] == '#':
            DFS(dx, dy)


T = int(input())
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]
ct = 0

for i in range(T):

    N, M = map(int, input().split())
    visited = [[0 for i in range(M)] for j in range(N)]
    arr = []
    for j in range(N):
        arr.append(input())

    for a in range(N):
        for b in range(M):
            if arr[a][b] == '#' and visited[a][b] == 0:
                DFS(a, b)
                ct += 1

    print(ct)
    ct = 0