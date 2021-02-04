def DFS(x, y):
    if x < 0 or x >= b or y < 0 or y >= a:
        return False

    if visited[x][y] == 0 and graph[x][y] == 1:
        visited[x][y] = 1
        graph[x][y] = 0
        DFS(x - 1, y - 1)
        DFS(x - 1, y)
        DFS(x - 1, y + 1)
        DFS(x, y + 1)
        DFS(x + 1, y + 1)
        DFS(x + 1, y)
        DFS(x + 1, y - 1)
        DFS(x, y - 1)
        return True

    return False


while True:

    a, b = map(int, input().split())
    graph = []
    visited = [[0 for i in range(a)] for j in range(b)]
    cnt = 0

    for i in range(b):
        graph.append(list(map(int, input().split())))

    if a == 0 and b == 0:
        break

    for i in range(b):
        for j in range(a):
            if DFS(i, j) == True:
                cnt += 1
    print(cnt)