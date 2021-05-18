from sys import stdin

N = int(stdin.readline())

for i in range(N):

    a = int(stdin.readline())
    Max = a

    while a != 1:

        if a % 2 == 0:
            a //= 2

        else:
            a = a * 3 + 1
            Max = max(a, Max)

    print(Max)