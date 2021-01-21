from collections import deque


def BFS(x, y):
    queue = deque()
    queue.append((x, y, 0))

    if x == c and y == d:
        print(0)
        return

    arr[x][y] = 1

    while queue:

        x, y, z = queue.popleft()
        if x == c and y == d:
            print(z)
            return

        for i in range(8):
            dx = x + nx[i]
            dy = y + ny[i]

            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue

            if arr[dx][dy] == 0:
                arr[dx][dy] = 1
                queue.append((dx, dy, z + 1))


nx = [-1, -2, -2, -1, 1, 2, 2, 1]
ny = [-2, -1, 1, 2, 2, 1, -1, -2]

T = int(input())
for i in range(T):
    N = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    arr = [[0 for i in range(N)] for j in range(N)]
    BFS(a, b)