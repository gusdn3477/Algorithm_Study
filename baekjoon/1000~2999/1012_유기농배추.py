import sys

sys.setrecursionlimit(10000)


def DFS(x, y):
    if (x < 0 or x >= N or y < 0 or y >= M):
        return False

    if (graph[x][y] == 1 and visited[x][y] == 0):
        visited[x][y] = 1
        DFS(x - 1, y)
        DFS(x, y - 1)
        DFS(x + 1, y)
        DFS(x, y + 1)
        return True

    return False


T = int(input())
for i in range(T):

    M, N, K = map(int, input().split())
    graph = [[0 for i in range(M)] for j in range(N)]
    visited = [[0 for i in range(M)] for j in range(N)]

    for j in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1

    count = 0
    for a in range(N):
        for b in range(M):
            if DFS(a, b) == True:
                count += 1

    print(count)