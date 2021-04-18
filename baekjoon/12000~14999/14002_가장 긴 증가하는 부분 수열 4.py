N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N
ans = []

for i in range(N):
    for j in range(i + 1, N):
        if arr[i] < arr[j]:
            dp[j] = max(dp[i] + 1, dp[j])

idx = dp.index(max(dp))
a = idx - 1
ans.append(arr[idx])
start = dp[idx] - 1

for i in range(a, -1, -1):

    if dp[i] == start:
        ans.append(arr[i])
        start -= 1

print(max(dp))
ans.reverse()
print(*ans)