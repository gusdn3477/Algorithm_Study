arr = []
N = int(input())
ct = 0

for i in range(N):
    arr.append(int(input()))

for i in range(len(arr) - 2, -1, -1):

    if arr[i] >= arr[i + 1]:
        ct += (arr[i] - arr[i + 1]) + 1
        arr[i] = arr[i + 1] - 1

print(ct)