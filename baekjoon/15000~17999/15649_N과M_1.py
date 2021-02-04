def DFS(count):
    if count == M:
        for i in pocket:
            print(i, end=' ')
        print()

    for i in range(1, N + 1):
        if visit[i] == 0:
            visit[i] = 1
            pocket.append(i)
            DFS(count + 1)
            visit[i] = 0
            pocket.pop()


N, M = map(int, input().split())
pocket = []
visit = [0] * (N + 1)

DFS(0)