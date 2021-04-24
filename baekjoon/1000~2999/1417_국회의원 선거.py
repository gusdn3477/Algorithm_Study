import heapq

N = int(input())
heap = []
ct = 0

dasom = int(input())
for i in range(N - 1):
    t = int(input())
    heapq.heappush(heap, [-t, t])

if N != 1:
    while dasom <= heap[0][1]:
        a = heapq.heappop(heap)
        heapq.heappush(heap, [a[0] + 1, a[1] - 1])
        ct += 1
        dasom += 1

print(ct)