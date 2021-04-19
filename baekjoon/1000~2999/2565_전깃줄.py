N = int(input())
arr = []
dp = [1] * N
dp2 = [1] * N
for i in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort()

for i in range(N):
    for j in range(i + 1, N):
        if arr[i][1] < arr[j][1]:
            dp[j] = max(dp[j], dp[i] + 1)

a = max(dp)
print(N - a)