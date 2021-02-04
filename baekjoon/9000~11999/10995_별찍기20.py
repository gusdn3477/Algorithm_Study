N = int(input())


def printStar(x):
    for i in range(x):
        print(' *', end='')
    print()


def printStar2(x):
    for i in range(x):
        print('* ', end='')
    print()


for i in range(1, N + 1):

    if i % 2 != 0:
        printStar2(N)

    else:
        printStar(N)