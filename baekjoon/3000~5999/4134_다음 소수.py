from math import sqrt


def isPrime(K):
    if K == 0 or K == 1:
        return False

    for i in range(2, int(sqrt(K)) + 1):
        if K % i == 0:
            return False

    return True


N = int(input())
for i in range(N):
    a = int(input())

    while True:
        if isPrime(a):
            print(a)
            break

        a += 1