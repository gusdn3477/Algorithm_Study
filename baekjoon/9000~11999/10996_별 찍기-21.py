def one(x):
    for i in range(int(x / 2 + 0.5)):
        print('*', end=' ')
    print()


def two(x):
    for i in range(x // 2):
        print(' *', end='')
    print()


N = int(input())

for i in range(N):
    one(N)
    two(N)