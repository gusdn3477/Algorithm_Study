N = int(input())
INF = int(1e9)
arr = []
ans = [[0 for i in range(N)] for j in range(N)]
M = 0

for i in range(N):
    ans[i][i] = 0

for i in range(N):
    arr.append(input())

for k in range(N):
    for i in range(N):
        for j in range(N):

            if i == j:
                continue

            if arr[i][j] == 'Y' or (arr[i][k] == 'Y' and arr[k][j] == 'Y'):
                ans[i][j] = 1

for i in range(N):
    M = max(M, sum(ans[i]))

print(M)