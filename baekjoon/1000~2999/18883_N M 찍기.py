N, M = map(int, input().split())

start = 1

while start <= N * M:

    for i in range(M):

        if i == M - 1:
            print(start)

        else:
            print(start, end=' ')

        start += 1
