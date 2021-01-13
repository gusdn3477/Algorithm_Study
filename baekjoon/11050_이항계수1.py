def recursive(N, K):
    if K == 0:
        return 1

    else:
        return N * recursive(N - 1, K - 1)


def recur(N):
    if N == 0 or N == 1:
        return 1

    else:
        return N * recur(N - 1)


N, K = map(int, input().split())
print(recursive(N, K) // recur(K))