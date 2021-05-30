from math import sqrt

arr = [0] * 10001
arr[0] = 1
arr[1] = 1
for i in range(2, int(sqrt(10001) + 1)):
    for j in range(i + i, 10001, i):
        if arr[j] == 0:
            arr[j] = 1

A = int(input())
B = int(input())

total = []
for i in range(A, B + 1):

    if arr[i] == 0:
        total.append(i)

if total:
    print(sum(total))
    print(min(total))

else:
    print(-1)