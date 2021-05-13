n, k = map(int, input().split())
dp = [[0 for i in range(n + 2)] for j in range(n + 2)]

dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1

for i in range(3, n + 1):
    for j in range(n + 2):

        if j == 1:
            dp[i][j] = 1

        elif j == n + 1:
            dp[i][j] = 1

        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

print(dp[n][k])