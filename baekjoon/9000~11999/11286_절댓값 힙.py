import heapq, sys

N = int(input())
heap = []

for i in range(N):

    a = sys.stdin.readline().rstrip()
    if a == '0':
        if not heap:
            print(0)

        else:
            print(heapq.heappop(heap)[1])

    else:
        heapq.heappush(heap, [abs(int(a)), int(a)])