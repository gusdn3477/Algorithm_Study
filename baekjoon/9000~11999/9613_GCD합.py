from itertools import combinations


def GCD(x, y):
    while x:
        x, y = y % x, x

    return y


N = int(input())

for i in range(N):
    total = 0
    arr = list(map(int, input().split()))
    arr = arr[1:]

    com = list(combinations(arr, 2))

    for j in range(len(com)):
        total += GCD(com[j][0], com[j][1])

    print(total)