dp = [0] * 252
dp[0] = 1
dp[1] = 1
dp[2] = 3

for i in range(3, 252):
    dp[i] = dp[i - 1] + 2 * dp[i - 2]

while True:

    try:
        N = int(input())

    except:
        break

    print(dp[N])