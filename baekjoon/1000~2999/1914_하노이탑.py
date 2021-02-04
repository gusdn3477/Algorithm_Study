def hanoi(N, start, mid, end):
    if N <= 20:
        if N == 1:
            print(start, end)

        else:
            hanoi(N - 1, start, end, mid)
            print(start, end)
            hanoi(N - 1, mid, start, end)


def total(N):
    return 2 ** N - 1


N = int(input())
M = total(N)
print(M)
hanoi(N, 1, 2, 3)