import heapq

N = int(input())
arr = []
total = 0

for i in range(N):
    heapq.heappush(arr, int(input()))

while len(arr) >= 2:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    total += (a + b)
    heapq.heappush(arr, a + b)

print(total)