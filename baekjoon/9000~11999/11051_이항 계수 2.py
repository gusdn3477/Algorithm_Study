N, K = map(int, input().split())
dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
dp[0][0] = 1
dp[1][0] = 1
dp[1][1] = 1

for i in range(2, N + 1):
    for j in range(N + 1):

        if j == 0:
            dp[i][j] = 1

        elif j == N:
            dp[i][j] = 1

        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

print(dp[N][K])