dp = [0] * 100001
N = int(input())

dp[1] = N

if N == 1:
    print(1)

else:
    for i in range(2, 100001):

        if dp[i - 1] % 2 == 0:
            dp[i] = dp[i - 1] // 2

        else:
            dp[i] = 3 * dp[i - 1] + 1

        if dp[i] == 1:
            save = i
            break

    print(save)