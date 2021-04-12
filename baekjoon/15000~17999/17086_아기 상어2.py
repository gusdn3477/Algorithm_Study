from collections import deque


def BFS(x, y, ct):
    global m
    queue = deque()
    queue.append((x, y, ct))
    visited[x][y] = 1

    while queue:

        a = queue.popleft()
        if arr[a[0]][a[1]] == 1:
            m = max(m, a[2])
            return

        for i in range(8):
            dx = a[0] + nx[i]
            dy = a[1] + ny[i]

            if dx < 0 or dx >= N or dy < 0 or dy >= M:
                continue

            if visited[dx][dy] == 0:
                visited[dx][dy] = 1
                queue.append((dx, dy, a[2] + 1))


N, M = map(int, input().split())
m = 0
arr = []
nx = [-1, -1, -1, 0, 1, 1, 1, 0]
ny = [-1, 0, 1, 1, 1, 0, -1, -1]
for i in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        visited = [[0 for i in range(M)] for j in range(N)]
        BFS(i, j, 0)

print(m)