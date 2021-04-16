N, M = map(int, input().split())
dp = [[0 for i in range(M)] for j in range(N)]
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

dp[0][0] = arr[0][0]
for i in range(N):
    for j in range(M):

        if i == 0 and j == 0:
            continue

        elif i == 0:
            dp[i][j] = max(dp[i][j - 1] + arr[i][j], dp[i][j])

        elif j == 0:
            dp[i][j] = max(dp[i - 1][j] + arr[i][j], dp[i][j])

        else:
            dp[i][j] = max(dp[i - 1][j] + arr[i][j], dp[i][j - 1] + arr[i][j], dp[i][j])

print(dp[N - 1][M - 1])
