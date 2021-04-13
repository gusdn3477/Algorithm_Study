from collections import deque


def BFS(x, y, ct):
    global c, d
    queue = deque()
    queue.append((x, y, ct))
    visited[x][y] = 1

    while queue:

        a = queue.popleft()
        dp[a[0]][a[1]] = a[2] + 1

        for i in range(8):
            dx = a[0] + nx[i]
            dy = a[1] + ny[i]

            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue

            if visited[dx][dy] == 0:
                visited[dx][dy] = 1
                queue.append((dx, dy, a[2] + 1))


N, M = map(int, input().split())
a, b = map(int, input().split())
nx = [-1, -2, -2, -1, 1, 2, 2, 1]
ny = [-2, -1, 1, 2, 2, 1, -1, -2]
dp = [[0 for _ in range(N)] for p in range(N)]
visited = [[0 for _ in range(N)] for p in range(N)]
BFS(a - 1, b - 1, -1)

for i in range(M):
    c, d = map(int, input().split())
    print(dp[c - 1][d - 1], end=' ')
