from collections import deque


def BFS(x, y):
    queue = deque([[x, y]])
    visited[x][y] = 1

    while queue:

        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                graph[nx][ny] = graph[a][b] + 1
                queue.append([nx, ny])


N, M = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

graph = []
visited = [[0 for i in range(M)] for j in range(N)]

for i in range(N):
    graph.append(list(map(int, input())))

BFS(0, 0)
print(graph[N - 1][M - 1])