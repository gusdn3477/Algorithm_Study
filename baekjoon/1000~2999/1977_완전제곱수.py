from math import sqrt

N = int(input())
M = int(input())
arr = []

for i in range(N, M + 1):
    if i / int(sqrt(i)) == int(sqrt(i)):
        arr.append(i)

if not arr:
    print(-1)

else:
    arr.sort()
    print(sum(arr))
    print(arr[0])