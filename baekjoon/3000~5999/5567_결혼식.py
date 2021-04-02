from collections import deque


def BFS(x, depth):
    global ct
    queue = deque()
    queue.append((x, depth))
    visited[x] = 1

    while queue:

        a = queue.pop()
        for i in range(1, N + 1):
            if arr[a[0]][i] == 1 and visited[i] == 0 and a[1] < 2:
                visited[i] = 1
                ct += 1
                queue.append((i, a[1] + 1))


N = int(input())
M = int(input())
ct = 0
visited = [0] * (N + 1)
arr = [[0 for i in range(N + 1)] for j in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

BFS(1, 0)
print(ct)