from itertools import permutations

N = int(input())
arr = [i for i in range(1,N+1)]

a = list(permutations(arr,N))
a.sort()

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
    print()