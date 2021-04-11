import sys

sys.setrecursionlimit(10000)


def DFS(x, y):
    global ct

    visited[x][y] = 1
    ct += 1

    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]

        if dx < 1 or dx > N or dy < 1 or dy > M:
            continue

        if visited[dx][dy] == 0 and arr[dx][dy] == 1:
            DFS(dx, dy)


N, M, K = map(int, input().split())
arr = [[0 for i in range(M + 1)] for j in range(N + 1)]
visited = [[0 for i in range(M + 1)] for j in range(N + 1)]

for i in range(K):
    a, b = map(int, input().split())
    arr[a][b] = 1

nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]
ct = 0
m = 0

for i in range(1, N + 1):
    for j in range(1, M + 1):
        ct = 0
        if arr[i][j] == 1 and visited[i][j] == 0:
            DFS(i, j)

        m = max(m, ct)

print(m)