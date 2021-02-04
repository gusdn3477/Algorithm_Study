from collections import deque


def BFS(x):
    queue = deque()
    queue.append((x, 0))
    visited[x] = 1

    while queue:

        x, y = queue.popleft()

        if x == b:
            poc.append(y)
            return

        for i in range(len(arr[x])):
            if arr[x][i] == 1 and visited[i] == 0:
                visited[i] = 1
                queue.append((i, y + 1))


N = int(input())

a, b = map(int, input().split())

K = int(input())
arr = [[0 for _ in range(N + 1)] for q in range(N + 1)]
poc = []
visited = [0 for _ in range(N + 1)]

for j in range(K):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1

BFS(a)

if not poc:
    print(-1)

else:
    print(poc[0])