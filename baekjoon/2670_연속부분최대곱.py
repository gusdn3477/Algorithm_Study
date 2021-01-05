N = int(input())
arr = []
dp = [0] * 10001

for i in range(N):
    arr.append(float(input()))

dp[0] = arr[0]

for i in range(1, N):
    for j in range(i):
        dp[i] = max(dp[j] * arr[i], arr[i])

print('%.3f' % (max(dp)))