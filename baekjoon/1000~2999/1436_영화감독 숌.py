from collections import deque

N = int(input())
queue = deque()
start = 666

while True:

    if str(start).count('666') >= 1:
        queue.append(str(start))

    start += 1

    if len(queue) == N:
        break

print(queue.pop())