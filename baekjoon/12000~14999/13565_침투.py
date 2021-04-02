from collections import deque


def DFS(x, y):
    stack = deque()
    stack.append((x, y))

    while stack:

        a = stack.pop()

        for i in range(4):
            dx = a[0] + nx[i]
            dy = a[1] + ny[i]

            if dx < 0 or dx >= N or dy < 0 or dy >= M:
                continue

            if arr[dx][dy] == '0' and visited[dx][dy] == 0:
                visited[dx][dy] = 1
                stack.append((a[0], a[1]))
                stack.append((dx, dy))
                break


N, M = map(int, input().split())
arr = []
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]
visited = [[0 for i in range(M)] for j in range(N)]
flag = 0

for i in range(N):
    arr.append(input())

for i in range(M):
    if arr[0][i] == '0':
        DFS(0, i)

for i in range(M):
    if visited[N - 1][i] == 1:
        flag = 1
        break

if flag:
    print("YES")

else:
    print('NO')