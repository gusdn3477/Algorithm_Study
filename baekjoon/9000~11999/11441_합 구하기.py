import sys

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * 100001
dp[0] = arr[0]

for i in range(1, len(arr)):
    dp[i] = dp[i - 1] + arr[i]

M = int(input())
for i in range(M):

    a, b = map(int, sys.stdin.readline().split())
    if a < 2:
        print(dp[b - 1])

    else:
        print(dp[b - 1] - dp[a - 2])