arr = [0 for i in range(0, 10001)]
N = int(input())

arr[0] = 0
arr[1] = 1

for i in range(2, 101):
    for j in range(i + i, 10001, i):
        if arr[j] == 0:
            arr[j] = 1

for i in range(N):
    M = int(input())
    a = 0
    b = 0
    for j in range((M // 2) + 1):
        if arr[j] == 0 and arr[M - j] == 0:
            a = j
            b = M - j

    print(a, b)