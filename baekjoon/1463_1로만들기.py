from collections import deque


def BFS(x):
    queue = deque()
    queue.append(x)

    while queue:

        if visited[1] != 0:
            break

        a = queue.popleft()

        if a % 3 == 0 and visited[a // 3] == 0:
            queue.append(a // 3)
            visited[a // 3] = visited[a] + 1

        if a % 2 == 0 and visited[a // 2] == 0:
            queue.append(a // 2)
            visited[a // 2] = visited[a] + 1

        if visited[a - 1] == 0:
            queue.append(a - 1)
            visited[a - 1] = visited[a] + 1


N = int(input())
arr = [0] * (N + 1)
visited = [0] * (N + 1)

if N == 1:
    print(0)

else:
    BFS(N)
    print(visited[1])