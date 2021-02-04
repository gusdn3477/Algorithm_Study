import sys

sys.setrecursionlimit(20000)


def DFS(x, y):
    global ct

    if arr[x][y] == 0:

        ct += 1
        arr[x][y] = 1
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]

            if dx < 0 or dx >= N or dy < 0 or dy >= M:
                continue

            if arr[dx][dy] == 0:
                DFS(dx, dy)

        return True


M, N, K = map(int, input().split())
arr = [[0 for i in range(M)] for j in range(N)]
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]
ct = 0
poc = []
check = 0

for i in range(K):
    a, b, c, d = map(int, input().split())

    for i in range(a, c):
        for j in range(b, d):
            arr[i][j] = 1

for i in range(N):
    for j in range(M):
        if DFS(i, j) == True:
            check += 1
            poc.append(ct)
            ct = 0

print(check)
poc.sort()
print(*poc)