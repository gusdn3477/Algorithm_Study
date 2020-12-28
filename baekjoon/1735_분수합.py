def GCD(x, y):
    if y == 0:
        return x

    else:
        return GCD(y, x % y)


A, B = map(int, input().split())
C, D = map(int, input().split())

up = A * D + B * C
down = B * D

k = GCD(up, down)

print(up // k, down // k)