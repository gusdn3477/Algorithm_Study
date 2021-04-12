from itertools import permutations

N, K = map(int, input().split())
arr = list(map(int, input().split()))
per = list(permutations(arr, N))
ct = 0

for i in range(len(per)):

    total = 500
    for j in range(len(per[i])):
        total += per[i][j] - K
        if total < 500:
            ct += 1
            break

print(len(per) - ct)