from sys import stdin
import heapq

heap = []
N = int(stdin.readline())

for i in range(N):

    a = int(stdin.readline())
    if a == 0:
        if not heap:
            print(0)

        else:
            print(heapq.heappop(heap))

    else:
        heapq.heappush(heap, a)