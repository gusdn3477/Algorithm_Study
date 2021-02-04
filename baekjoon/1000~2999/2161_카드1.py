from collections import deque

N = int(input())
queue = deque()

for i in range(1, N + 1):
    queue.append(i)

while queue:
    trash = queue.popleft()
    print(trash, end=' ')

    if not queue:
        break

    a = queue.popleft()
    queue.append(a)