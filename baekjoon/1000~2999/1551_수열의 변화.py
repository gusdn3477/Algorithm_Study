from copy import copy

N, K = map(int, input().split())
arr = input().split(',')
arr = list(map(int, arr))
start = 0

while start < K:

    arr2 = []
    for i in range(1, len(arr)):
        arr2.append(arr[i] - arr[i - 1])

    arr = copy(arr2)
    start += 1

arr = list(map(str, arr))
arr = ','.join(arr)
print(arr)