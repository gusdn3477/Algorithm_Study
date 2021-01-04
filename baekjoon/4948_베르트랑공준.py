from math import sqrt

arr = [i for i in range(250000)]
arr[0] = 0
arr[1] = 0

for i in range(2, int(sqrt(250000)) + 1):
    for j in range(i + i, 250000, i):
        if arr[j] != 0:
            arr[j] = 0

while True:

    N = int(input())
    ct = 0

    if N == 0:
        break

    for i in range(N + 1, N * 2 + 1):
        if arr[i] != 0:
            ct += 1

    print(ct)
