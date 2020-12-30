N = int(input())

for i in range(1, N + 1):

    if i == 1:
        for j in range(N - i, 0, -1):
            print(' ', end='')
        print('*')

    elif i == N:
        for j in range(N * 2 - 1):
            print('*', end='')

    else:
        for j in range(N - i, 0, -1):
            print(' ', end='')

        print('*', end='')
        for j in range(2 * (i - 1) - 1):
            print(' ', end='')
        print('*')