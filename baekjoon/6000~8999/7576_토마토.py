from collections import deque
from sys import stdin


def isAll():
    global N, M

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                return False

    return True


def isZero():
    global N, M

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                return True

    return False


def BFS(x, y, ct):
    global total

    # 처음에 다 차있는 경우
    if isAll():
        print(0)
        return True

    while queue:

        a = queue.popleft()
        visited[a[0]][a[1]] = 1

        for i in range(4):
            dx = a[0] + nx[i]
            dy = a[1] + ny[i]

            if dx < 0 or dx >= N or dy < 0 or dy >= M:
                continue

            if arr[dx][dy] == 0 and visited[dx][dy] == 0:
                visited[dx][dy] = 1
                arr[dx][dy] = 1
                queue.append((dx, dy, a[2] + 1))

                total = max(ct, a[2] + 1)

    return False


M, N = map(int, input().split())
arr = []
total = 0
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]
visited = [[0 for i in range(M)] for j in range(N)]
queue = deque()

for i in range(N):
    arr.append(list(map(int, stdin.readline().split())))

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append((i, j, 0))

if BFS(0, 0, 0):
    pass

elif isZero():
    print(-1)

else:
    print(total)