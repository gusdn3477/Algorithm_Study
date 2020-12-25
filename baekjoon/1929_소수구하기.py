from math import sqrt


def isPrime(n):
    if n == 1:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


N, M = map(int, input().split())

for i in range(N, M + 1):
    if isPrime(i) == True:
        print(i)