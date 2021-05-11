from collections import deque


def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    nx = [-2, -2, 0, 0, 2, 2]
    ny = [-1, 1, -2, 2, -1, 1]
    dp[x][y] = 0

    while queue:

        a = queue.popleft()
        if a[0] == c and a[1] == d:
            return

        for i in range(6):
            dx = a[0] + nx[i]
            dy = a[1] + ny[i]

            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue

            if dp[dx][dy] == -1:
                dp[dx][dy] = dp[a[0]][a[1]] + 1
                queue.append((dx, dy))


N = int(input())
dp = [[-1 for i in range(200)] for j in range(200)]
a, b, c, d = map(int, input().split())
BFS(a, b)
print(dp[c][d])
