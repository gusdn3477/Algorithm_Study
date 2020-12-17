def DFS(x, y):
    global cnt
    if x < 0 or x >= N or y < 0 or y >= N:
        return 0

    if visited[x][y] == 1:
        return 0

    if graph[x][y] == 1:
        visited[x][y] = 1
        graph[x][y] = 0
        cnt += 1
        DFS(x - 1, y)
        DFS(x, y - 1)
        DFS(x + 1, y)
        DFS(x, y + 1)
        return 1

    return 0


N = int(input())
graph = []
answer = []
visited = [[0 for i in range(N)] for j in range(N)]
cnt = 0
total = 0

for i in range(N):
    graph.append(list(map(int, input())))

for i in range(N):
    for j in range(N):
        if DFS(i, j) == 1:
            answer.append(cnt)
            total += 1
            cnt = 0

print(total)
answer.sort()
for i in range(len(answer)):
    print(answer[i])