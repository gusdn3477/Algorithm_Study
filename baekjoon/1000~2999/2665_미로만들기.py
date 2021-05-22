from collections import deque


def BFS(x, y, ct):
    queue = deque()
    queue.append((x, y, ct))
    visited[x][y] = 1

    nx = [-1, 0, 1, 0]
    ny = [0, -1, 0, 1]

    while queue:

        a = queue.popleft()

        if a[0] == N - 1 and a[1] == N - 1:
            print(a[2])
            return

        for i in range(4):
            dx = a[0] + nx[i]
            dy = a[1] + ny[i]

            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue

            if arr[dx][dy] == '1' and visited[dx][dy] == 0:
                visited[dx][dy] = 1
                queue.appendleft((dx, dy, a[2]))

            elif arr[dx][dy] == '0' and visited[dx][dy] == 0:
                visited[dx][dy] = 1
                queue.append((dx, dy, a[2] + 1))


N = int(input())
arr = []
visited = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    arr.append(input())

BFS(0, 0, 0)
