N = int(input())
arr = list(map(int, input().split()))
total = 0
dp = [0] * len(arr)
dp[0] = arr[0]

for i in range(1, len(arr)):
    dp[i] = dp[i - 1] + arr[i]

for i in range(len(arr) - 1):
    total += arr[i] * (dp[len(arr) - 1] - dp[i])

print(total)