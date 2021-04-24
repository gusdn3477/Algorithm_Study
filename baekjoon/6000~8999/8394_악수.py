N = int(input())
dp = [0] * (N + 4)
dp[1] = 0
dp[2] = 2
dp[3] = 3

for i in range(4, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10

print(dp[N] % 10)