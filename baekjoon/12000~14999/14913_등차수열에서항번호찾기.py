N, M, K = map(int, input().split())

if (K - N) % M != 0 or (N < K and M < 0) or (N > K and M > 0):
    print('X')

else:
    print((K - N) // M + 1)