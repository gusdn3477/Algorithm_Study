N, M = map(int, input().split())
INF = int(1e9)
arr = [[INF for i in range(N + 1)] for j in range(N + 1)]
m = int(1e9)
for i in range(1, N + 1):
    arr[i][i] = 0

for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in range(N + 1):
    for j in range(N + 1):
        if arr[i][j] == INF:
            arr[i][j] = 0

for i in range(1, N + 1):
    t = sum(arr[i])
    m = min(m, t)

for i in range(1, N + 1):
    if m == sum(arr[i]):
        print(i)
        break