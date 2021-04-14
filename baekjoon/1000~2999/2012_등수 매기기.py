N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))

arr.sort()
ans = [i for i in range(1, N + 1)]
total = 0

for i in range(N):
    total += abs(arr[i] - ans[i])

print(total)