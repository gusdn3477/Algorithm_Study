def GCD(x, y):
    if y == 0:
        return x

    else:
        return GCD(y, x % y)


a = list(map(int, input().split(':')))

k = GCD(a[0], a[1])
st = f'{a[0] // k}:{a[1] // k}'
print(st)