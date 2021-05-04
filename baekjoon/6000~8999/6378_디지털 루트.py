while True:

    N = int(input())
    if N == 0:
        break

    a = N
    while True:

        total = 0
        while a > 0:
            total += a % 10
            a //= 10

        if total < 10:
            print(total)
            break

        else:
            a = total