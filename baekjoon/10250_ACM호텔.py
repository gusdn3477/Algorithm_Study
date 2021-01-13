from math import ceil

N = int(input())

for i in range(N):
    H, W, T = map(int, input().split())

    if T % H == 0:
        print(H, end='')

    else:
        print(T % H, end='')

    t = ceil(T / H)
    t = str(t)

    if len(t) == 1:
        print('0', end='')
        print(t)

    else:
        print(t)