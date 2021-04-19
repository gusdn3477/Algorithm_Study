from collections import deque


def BFS(x):
    global A, ct

    queue = deque()
    queue.append((x, 1))

    while queue:

        a = queue.popleft()

        if a[0] == A:
            ct = a[1]
            return

        if a[0] % 10 == 1 and a[0] // 10 >= A:
            queue.append((a[0] // 10, a[1] + 1))

        elif a[0] % 2 == 0 and a[0] // 2 >= A:
            queue.append((a[0] // 2, a[1] + 1))


A, B = map(int, input().split())
ct = -1
BFS(B)
print(ct)