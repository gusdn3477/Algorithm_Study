N = int(input())
dp = [0] * 1000001

dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(N):

    M = int(input())
    for i in range(4,M+1):
        dp[i] = dp[i-1] % 1000000009 + dp[i-2] % 1000000009 + dp[i-3] % 1000000009

    print(dp[M]% 1000000009)