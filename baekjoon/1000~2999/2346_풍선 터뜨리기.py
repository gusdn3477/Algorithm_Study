from collections import deque

N = int(input())
arr = list(map(int, input().split()))
queue = deque()

for i in range(len(arr)):
    queue.append([i + 1, arr[i]])

while True:

    a = queue.popleft()
    print(a[0], end=' ')

    if not queue:
        break

    if a[1] > 0:
        for i in range(a[1] - 1):
            tmp = queue.popleft()
            queue.append(tmp)

    elif a[1] < 0:
        for i in range(abs(a[1])):
            tmp = queue.pop()
            queue.appendleft(tmp)