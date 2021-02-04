N = int(input())
poc = list(map(int, input().split()))
dp = [0] * N
dp[0] = poc[0]

for i in range(1, N):
    dp[i] = max(dp[i - 1] + poc[i], poc[i])

print(max(dp))