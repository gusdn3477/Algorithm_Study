N = int(input())

for i in range(N):

    a = input().split()
    t = float(a[0])
    for i in range(1, len(a)):

        if a[i] == '@':
            t *= 3

        elif a[i] == '%':
            t += 5

        elif a[i] == '#':
            t -= 7

    print('%.2f' % t)