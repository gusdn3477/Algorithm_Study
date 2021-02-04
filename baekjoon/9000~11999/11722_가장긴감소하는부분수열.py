N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N

for i in range(1, len(arr)):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))