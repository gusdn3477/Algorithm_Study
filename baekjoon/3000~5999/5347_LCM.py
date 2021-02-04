def GCD(x, y):
    if y == 0:
        return x;

    else:
        return GCD(y, x % y)


N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    print(a * b // GCD(a, b))