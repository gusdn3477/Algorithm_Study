def DFS(x):
    visited[x] = 1
    for i in range(1, N + 1):
        if arr[x][i] == 1 and visited[i] == 0:
            DFS(i)


N, M = map(int, input().split())

arr = [[0 for i in range(N + 1)] for j in range(N + 1)]
visited = [0] * (N + 1)
ct = 0

for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

for i in range(1, N + 1):

    if visited[i] == 0:
        DFS(i)
        ct += 1

print(ct)