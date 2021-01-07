def SelfNum(n):
    a = 0
    a += n

    while n > 0:
        a += n % 10
        n = n // 10

    return a


arr = [0] * 10001

for i in range(1, 10001):
    a = SelfNum(i)

    while a <= 10000:
        arr[a] = 1
        a = SelfNum(a)

for i in range(1, 10001):

    if arr[i] == 0:
        print(i)