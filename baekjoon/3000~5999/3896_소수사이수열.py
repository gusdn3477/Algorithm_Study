from math import sqrt

arr = [0] * 1299710
arr[0] = 1
arr[1] = 1

for i in range(2, int(sqrt(1299710) + 1)):
    for j in range(i + i, 1299710, i):
        if arr[j] == 0:
            arr[j] = 1

N = int(input())

for i in range(N):

    K = int(input())
    ct = 0
    ct = 0

    if arr[K] == 0:
        print(0)

    else:
        for x in range(K + 1, 1299710):
            if arr[x] == 0:
                ct = x
                break

        for x in range(K, 1, -1):
            if arr[x] == 0:
                ct2 = x
                break

        print(ct - ct2)