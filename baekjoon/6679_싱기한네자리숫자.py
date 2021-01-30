for i in range(1000, 10000):
    a = 0
    b = 0
    c = 0

    save = i
    save2 = i
    save3 = i

    while save > 0:
        a += save % 10
        save //= 10

    while save2 > 0:
        b += save2 % 12
        save2 //= 12

    while save3 > 0:
        c += save3 % 16
        save3 //= 16

    if a == b and b == c:
        print(i)