from collections import deque


def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    global total_lamb, total_wolf

    lamb, wolf = 0, 0

    if arr[x][y] == 'v':
        wolf += 1

    elif arr[x][y] == 'o':
        lamb += 1

    while queue:

        a = queue.popleft()

        for i in range(4):

            dx = a[0] + nx[i]
            dy = a[1] + ny[i]

            if dx < 0 or dx >= R or dy < 0 or dy >= C:
                continue

            if arr[dx][dy] == 'v' and visited[dx][dy] == 0:
                visited[dx][dy] = 1
                wolf += 1
                queue.append((dx, dy))

            elif arr[dx][dy] == 'o' and visited[dx][dy] == 0:
                visited[dx][dy] = 1
                lamb += 1
                queue.append((dx, dy))

            elif arr[dx][dy] == '.' and visited[dx][dy] == 0:
                visited[dx][dy] = 1
                queue.append((dx, dy))

    if lamb > wolf:
        total_lamb += lamb

    else:
        total_wolf += wolf


R, C = map(int, input().split())
arr = []
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]
total_lamb = 0
total_wolf = 0

visited = [[0 for i in range(C)] for j in range(R)]

for i in range(R):
    arr.append(input())

for i in range(R):
    for j in range(C):
        if arr[i][j] != '#' and visited[i][j] == 0:
            BFS(i, j)

print(total_lamb, total_wolf)