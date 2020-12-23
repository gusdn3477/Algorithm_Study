def DFS(count):
    if count == M:
        for i in pocket:
            print(i, end=' ')
        print()
        return

    for i in range(1, N + 1):

        if not pocket and visited[i] == 0:
            visited[i] = 1
            pocket.append(i)
            DFS(count + 1)
            visited[i] = 0
            pocket.pop()

        elif pocket[-1] < i and visited[i] == 0:
            visited[i] = 1
            pocket.append(i)
            DFS(count + 1)
            visited[i] = 0
            pocket.pop()


N, M = map(int, input().split())

visited = [0] * (N + 1)
pocket = []
DFS(0)