from collections import deque


def BFS(x, y):
    global total_v, total_k
    queue = deque()
    queue.append((x, y))
    v = 0
    k = 0

    visited[x][y] = 1
    if arr[x][y] == 'v':
        v += 1

    elif arr[x][y] == 'k':
        k += 1

    while queue:

        a = queue.popleft()

        for i in range(4):
            dx = a[0] + nx[i]
            dy = a[1] + ny[i]

            if dx < 0 or dx >= N or dy < 0 or dy >= M:
                continue

            if arr[dx][dy] != '#' and visited[dx][dy] == 0:
                visited[dx][dy] = 1

                if arr[dx][dy] == 'v':
                    v += 1

                elif arr[dx][dy] == 'k':
                    k += 1

                queue.append((dx, dy))

    if v >= k:
        total_v += v

    else:
        total_k += k


N, M = map(int, input().split())
arr = []
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]
visited = [[0 for i in range(M)] for j in range(N)]
total_v = 0
total_k = 0

for i in range(N):
    arr.append(input())

for i in range(N):
    for j in range(M):
        if arr[i][j] != '#' and visited[i][j] == 0:
            BFS(i, j)

print(total_k, total_v)