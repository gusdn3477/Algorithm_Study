from heapq import heappush, heappop
from sys import stdin

N = int(stdin.readline())
heap = []

for i in range(N):
    M = int(stdin.readline())

    if M == 0 and not heap:
        print(0)

    elif M == 0:
        print(heap[0][1])
        heappop(heap)

    else:
        heappush(heap, (-M, M))