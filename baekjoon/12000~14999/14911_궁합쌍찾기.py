from itertools import combinations

a = list(map(int, input().split()))
b = int(input())
ct = 0

arr = list(combinations(a, 2))
arr = list(set(arr))
arr.sort()

for i in range(len(arr)):
    if sum(arr[i]) == b:
        print(*arr[i])
        ct += 1

print(ct)