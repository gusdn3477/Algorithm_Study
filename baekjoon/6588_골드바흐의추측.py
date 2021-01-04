from math import sqrt

arr = [i for i in range(1000001)]
arr[0] = 0
arr[1] = 0

for i in range(2, int(sqrt(1000001)) + 1):
    for j in range(i + i, 1000001, i):
        if arr[j] != 0:
            arr[j] = 0

while True:

    N = int(input())
    if N == 0:
        break

    for i in range(2, N + 1):
        if arr[i] != 0 and arr[N - i] != 0:
            print(str(N), '=', arr[i], '+', arr[N - i])
            break

        if i == N:
            print("Goldbach's conjecture is wrong")
            break