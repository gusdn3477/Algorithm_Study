while True:

    a = int(input())
    arr = []

    if a == 0:
        break

    arr.append(a)

    while len(str(arr[-1])) > 1:

        t = arr[-1]
        start = 1

        while t > 0:
            start *= t % 10
            t //= 10

        arr.append(start)

    print(*arr)