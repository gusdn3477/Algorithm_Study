def GCD(x, y):
    if y == 0:
        return x

    else:
        return GCD(y, x % y)


s = input()
t = input()

if len(s) == len(t):

    if s == t:
        print(1)

    else:
        print(0)

else:

    a = GCD(len(s), len(t))
    b = len(s) * len(t) // a

    s = s * (b // len(s))
    t = t * (b // len(t))

    if s == t:
        print(1)

    else:
        print(0)