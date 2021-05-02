N = int(input())
M = int(input())
INF = int(1e9)

arr = [[INF for i in range(N + 1)] for j in range(N + 1)]

for i in range(1, N + 1):
    arr[i][i] = 0

for i in range(M):
    a, b, c = map(int, input().split())
    arr[a][b] = min(c, arr[a][b])

for i in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            arr[a][b] = min(arr[a][b], arr[a][i] + arr[i][b])

for i in range(1, N + 1):
    for j in range(1, N + 1):

        if arr[i][j] == INF:
            print(0, end=' ')

        else:
            print(arr[i][j], end=' ')
    print()