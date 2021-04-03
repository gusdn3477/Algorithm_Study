from collections import deque


def BFS(x, y):
    global ct
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    ct += 1

    while queue:

        a = queue.popleft()

        for i in range(4):
            dx = a[0] + nx[i]
            dy = a[1] + ny[i]

            if dx < 0 or dx >= N or dy < 0 or dy >= M:
                continue

            if arr[dx][dy] == '1' and visited[dx][dy] == 0:
                visited[dx][dy] = 1
                queue.append((dx, dy))
                ct += 1


N, M = map(int, input().split())
arr = []
ans = 0
ct = 0
ct2 = 0
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]
visited = [[0 for i in range(M)] for j in range(N)]

for i in range(N):
    arr.append(input().split())

for i in range(N):
    for j in range(M):
        if arr[i][j] == '1' and visited[i][j] == 0:
            BFS(i, j)
            ct2 += 1
            ans = max(ans, ct)
            ct = 0

print(ct2, ans)