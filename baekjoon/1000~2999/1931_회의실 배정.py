N = int(input())
arr = []
ct_max = 0

for i in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

arr = sorted(arr, key=lambda x: (x[1], x[0]))

ct = 1
start = arr[0]

for i in range(1, N):
    if arr[i][0] >= start[1]:
        ct += 1
        start = arr[i]

print(ct)