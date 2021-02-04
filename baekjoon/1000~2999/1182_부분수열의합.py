from itertools import combinations

A, B = map(int, input().split())
arr = list(map(int, input().split()))
ct = 0

for i in range(1, len(arr) + 1):
    poc = list(combinations(arr, i))
    for j in poc:
        if sum(j) == B:
            ct += 1

print(ct)