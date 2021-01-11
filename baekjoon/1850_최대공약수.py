def GCD(x, y):
    if y == 0:
        return x

    else:
        return GCD(y, x % y)


A, B = map(int, input().split())
g = GCD(A, B)

print('1' * g)