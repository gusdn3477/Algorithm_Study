from collections import deque


def BFS(x, t):
    queue = deque()
    queue.append((x, t))
    visited[x] = 1

    while queue:

        a = queue.popleft()
        if a[0] == K:
            return a[1]

        if a[0] * 2 <= 100000 and visited[a[0] * 2] == 0:
            visited[a[0] * 2] = 1
            queue.appendleft((a[0] * 2, a[1]))

        if a[0] + 1 <= 100000 and visited[a[0] + 1] == 0:
            visited[a[0] + 1] = 1
            queue.append((a[0] + 1, a[1] + 1))

        if a[0] - 1 >= 0 and visited[a[0] - 1] == 0:
            visited[a[0] - 1] = 1
            queue.append((a[0] - 1, a[1] + 1))


N, K = map(int, input().split())
visited = [0] * 100001
a = BFS(N, 0)
print(a)