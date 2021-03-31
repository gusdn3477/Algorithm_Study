E, S, M = map(int, input().split())
a, b, c = 1, 1, 1
start = 1
while True:

    if E == a and S == b and M == c:
        print(start)
        break

    a += 1
    b += 1
    c += 1

    if a > 15:
        a = 1

    if b > 28:
        b = 1

    if c > 19:
        c = 1

    start += 1