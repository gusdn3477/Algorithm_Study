N = int(input())

for i in range(1, N + 1):

    if i == 1:
        for j in range(N - i, 0, -1):
            print(' ', end='')
        print('*')

    else:
        for j in range(N - i, 0, -1):
            print(' ', end='')

        for j in range(i):
            print('* ', end='')
        print('')