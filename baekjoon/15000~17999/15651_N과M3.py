def DFS(count):
    if count == M:
        for i in pocket:
            print(i, end=' ')
        print()
        return

    for i in range(1, N + 1):
        pocket.append(i)
        DFS(count + 1)
        pocket.pop()


N, M = map(int, input().split())

pocket = []
visited = [0] * (N + 1)
DFS(0)