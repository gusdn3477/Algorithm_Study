N = int(input())
arr = list(map(int, input().split()))
total = 0
dp = [0] * N
dp[0] = arr[0]

for i in range(1, N):
    dp[i] = dp[i - 1] + arr[i]

for i in range(N - 1):
    total += arr[i] * (dp[N - 1] - dp[i])

print(total)