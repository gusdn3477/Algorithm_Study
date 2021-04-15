def GCD(x, y):
    while y > 0:
        x, y = y, x % y

    return x


N, M = map(int, input().split())
g = GCD(N, M)

for i in range(1, g + 1):

    if g % i == 0:
        print(i, N // i, M // i)