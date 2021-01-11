def GCD(x, y):
    if y == 0:
        return x

    else:
        return GCD(y, x % y)


A, B = map(int, input().split())
C = GCD(A, B)
print(A * B // C)