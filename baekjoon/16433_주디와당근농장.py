import sys

sys.setrecursionlimit(10000)


def DFS(a, b):
    if a <= 0 or a > N or b <= 0 or b > N:
        return

    if visited[a][b] != 0:
        return

    if visited[a][b] == 0:
        m[a][b] += 1
        visited[a][b] = 1
        DFS(a - 1, b - 1)
        DFS(a - 1, b + 1)
        DFS(a + 1, b + 1)
        DFS(a + 1, b - 1)


N, a, b = map(int, input().split())
m = [[0 for i in range(N + 1)] for j in range(N + 1)]
visited = [[0 for i in range(N + 1)] for j in range(N + 1)]
DFS(a, b)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if m[i][j] == 0:
            print('.', end='')

        else:
            print('v', end='')
    print()