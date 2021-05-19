N = int(input())
arr = []
INF = int(1e9)

for i in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            arr[i][j] = INF

for k in range(N):
    for i in range(N):
        for j in range(N):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in range(N):
    for j in range(N):

        if arr[i][j] == INF:
            print(0, end=' ')

        else:
            print(1, end=' ')
    print()