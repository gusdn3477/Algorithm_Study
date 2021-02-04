from collections import deque


def BFS(x):
    global t
    queue = deque()
    queue.append(x)
    arr[x] = 1

    while queue:

        a = queue.popleft()
        if a == M:
            return

        elif a > M:

            if a - 1 >= 0:
                if arr[a - 1] == 0:
                    queue.append(a - 1)
                    arr[a - 1] += arr[a] + 1

        else:
            if a - 1 >= 0:
                if arr[a - 1] == 0:
                    queue.append(a - 1)
                    arr[a - 1] += arr[a] + 1

            if a * 2 <= 100001:
                if arr[a * 2] == 0:
                    queue.append(a * 2)
                    arr[a * 2] += arr[a] + 1

            if a + 1 <= 100001:
                if arr[a + 1] == 0:
                    queue.append(a + 1)
                    arr[a + 1] += arr[a] + 1


t = 0
N, M = map(int, input().split())
arr = [0] * 100001
BFS(N)
print(arr[M] - 1)