from math import sqrt

while True:

    N = int(input())
    poc = []

    if N == -1:
        break

    for i in range(1, int(sqrt(N)) + 1):
        if N % i == 0:
            if i * i != N:
                poc.append(i)
                poc.append(N // i)

            else:
                poc.append(i)

    poc.remove(N)
    poc.sort()

    if sum(poc) == N:
        print(N, '=', end=' ')
        for i in range(len(poc)):
            print(poc[i], end=' ')

            if i != len(poc) - 1:
                print('+', end=' ')
        print()

    else:
        print(N, 'is NOT perfect.')