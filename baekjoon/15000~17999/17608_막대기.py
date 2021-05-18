from collections import deque

N = int(input())
queue = deque()
ct = 1

for i in range(N):
    queue.append(int(input()))

start = queue.pop()

while queue:

    a = queue.pop()
    if a > start:
        start = a
        ct += 1

print(ct)