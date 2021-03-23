from math import sqrt


def isPrime(N):
    for i in range(2, int(sqrt(N)) + 1):
        if N % i == 0:
            return False

    return True


N = int(input())

if N == 1:
    print(2)

else:
    while True:

        a = str(N)
        if a == a[::-1] and isPrime(N):
            print(N)
            break
        N += 1