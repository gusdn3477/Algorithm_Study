def printJ(N):
    for i in range(N):
        print('J', end='')


M = int(input())

for k in range(M):
    N = int(input())

    for i in range(1, N + 1):

        if i == 1 or i == N:

            for j in range(N):
                print('#', end='')
            print('')

        else:
            print('#', end='')
            printJ(N - 2)
            print('#')

    print()