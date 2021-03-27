import heapq

heap = []
N = int(input())

for i in range(N):
    arr = list(map(int, input().split()))

    for j in arr:
        if len(heap) < N:
            heapq.heappush(heap, j)

        else:
            heapq.heappush(heap, j)
            heapq.heappop(heap)

print(heap[0])