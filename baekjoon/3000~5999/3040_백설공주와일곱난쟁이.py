from itertools import combinations

poc = []

for i in range(9):
    poc.append(int(input()))

a = list(combinations(poc,7))

for i in range(len(a)):
    if sum(a[i]) == 100:
        for j in range(len(a[i])):
            print(a[i][j])
        break