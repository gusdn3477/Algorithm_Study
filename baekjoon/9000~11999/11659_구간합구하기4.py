import sys

N, M = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * 100001
dp[0] = arr[0]

for i in range(1, N):
    dp[i] = dp[i - 1] + arr[i]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if a - 2 < 0:
        x = 0

    else:
        x = dp[a - 2]

    print(dp[b - 1] - x)