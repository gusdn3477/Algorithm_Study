def DFS(x, y, ch):
    global ct
    visited[x][y] = 1
    ct += 1

    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]

        if dx < 0 or dx >= M or dy < 0 or dy >= N:
            continue

        if visited[dx][dy] == 0 and arr[dx][dy] == ch:
            DFS(dx, dy, ch)


N, M = map(int, input().split())
arr = []
ct = 0
a, b = 0, 0
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]
visited = [[0 for i in range(N)] for j in range(M)]
for i in range(M):
    arr.append(input())

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0 and arr[i][j] == 'W':
            DFS(i, j, 'W')
            a += ct ** 2
            ct = 0

ct = 0
visited = [[0 for i in range(N)] for j in range(M)]
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0 and arr[i][j] == 'B':
            DFS(i, j, 'B')
            b += ct ** 2
            ct = 0

ct = 0
print(a, b)