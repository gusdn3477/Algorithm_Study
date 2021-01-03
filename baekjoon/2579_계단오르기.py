N = int(input())
dp = [0] * 301
arr = [0] * 301

for i in range(N):
    arr[i] = int(input())

dp[0] = arr[0]
dp[1] = max(dp[0] + arr[1], arr[1])
dp[2] = max(dp[0] + arr[2], arr[1] + arr[2])

for n in range(3, N):
    dp[n] = max(dp[n - 2] + arr[n], dp[n - 3] + arr[n - 1] + arr[n])

print(dp[N - 1])