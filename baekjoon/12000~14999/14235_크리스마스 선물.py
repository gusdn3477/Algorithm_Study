import heapq

N = int(input())
heap = []

for i in range(N):

    a = list(map(int, input().split()))

    if a[0] == 0:

        if heap:
            a = heapq.heappop(heap)
            print(a[1])

        else:
            print(-1)

    else:
        for j in range(1, len(a)):
            heapq.heappush(heap, (-a[j], a[j]))