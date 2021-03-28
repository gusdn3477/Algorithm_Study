from collections import deque


def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:

        a = queue.popleft()

        for i in range(4):
            dx = a[0] + nx[i]
            dy = a[1] + ny[i]

            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue

            if arr[dx][dy] in color and visited[dx][dy] == 0:
                visited[dx][dy] = 1
                queue.append((dx, dy))

    return True


N = int(input())
arr = []
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]
ct = 0
ct2 = 0
for i in range(N):
    arr.append(input())

# 색맹인 경우 blue와 나머지 인식. blue
color = "RG"
visited = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] in color and visited[i][j] == 0:
            BFS(i, j)
            ct += 1

color = 'B'
visited = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] in color and visited[i][j] == 0:
            BFS(i, j)
            ct += 1

# 색맹이 아닌 경우
color = "R"
visited = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] in color and visited[i][j] == 0:
            BFS(i, j)
            ct2 += 1

color = 'G'
visited = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] in color and visited[i][j] == 0:
            BFS(i, j)
            ct2 += 1

color = "B"
visited = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] in color and visited[i][j] == 0:
            BFS(i, j)
            ct2 += 1

print(ct2, ct)