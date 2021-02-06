def GCD(x, y):
    while x:
        x, y = y % x, x

    return y


N = int(input())
arr = list(map(int, input().split()))

for i in range(1, len(arr)):
    a = GCD(arr[0], arr[i])
    print('%d/%d' % (arr[0] // a, arr[i] // a))