N = int(input())
a = 0
b = 0
flag = 0

if N < 5 and N % 2 != 0:
    print(-1)

elif (N % 5) % 2 == 0:
    a = N // 5
    N = N % 5
    b = N // 2
    print(a + b)

elif (N % 5) % 2 != 0:

    a = (N // 5) - 1
    N = N - 5 * a
    b = N // 2
    print(a + b)