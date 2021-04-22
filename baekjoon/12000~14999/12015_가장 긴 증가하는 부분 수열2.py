from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))
dp = []

dp.append(arr[0])

for i in range(1, len(arr)):

    a = bisect_left(dp, arr[i])
    if a == len(dp):
        dp.append(arr[i])

    else:
        dp[a] = arr[i]

print(len(dp))