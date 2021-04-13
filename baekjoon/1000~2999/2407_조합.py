n, m = map(int, input().split())

arr = [i for i in range(n, n - m, -1)]
arr2 = [i for i in range(1, m + 1)]

total = 1
total2 = 1

for i in arr:
    total *= i

for i in arr2:
    total2 *= i

print(total // total2)