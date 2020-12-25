def GCD(x, y):
    if y == 0:
        return x;

    else:
        return GCD(y, x % y)


N, M = map(int, input().split())
a = GCD(N, M)
print(a)
print(N * M // a)