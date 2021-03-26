T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    arr = [[0 for i in range(N + 1)] for j in range(N + 1)]

    for j in range(M):
        a, b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1

    print(N - 1)