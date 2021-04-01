def DFS(x, N):
    visited[x] = 1

    for i in range(1, N + 1):
        if visited[i] == 0 and arr[x][i] == 1:
            DFS(i, N)


T = int(input())
for i in range(T):
    N = int(input())
    arr = [[0 for i in range(N + 1)] for j in range(N + 1)]
    inp = list(map(int, input().split()))
    ct = 0

    for j in range(1, N + 1):
        arr[j][inp[j - 1]] = 1
        arr[inp[j - 1]][j] = 1

    visited = [0 for _ in range(N + 1)]
    for j in range(1, N + 1):
        if visited[j] == 0:
            DFS(j, N)
            ct += 1

    print(ct)