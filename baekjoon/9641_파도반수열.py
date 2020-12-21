P = [0] * 101

P[1] = 1
P[2] = 1
P[3] = 1

T = int(input())

for i in range(T):
    N = int(input())
    for j in range(4, N + 1):
        P[j] = P[j - 2] + P[j - 3]

    print(P[N])