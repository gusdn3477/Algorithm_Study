N = int(input())
dp = [1] * (N + 1)
poc = list(map(int, input().split()))

for i in range(N):
    for j in range(0, i):
        if poc[i] > poc[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))