import heapq


def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])
    distance[start] = 0

    while heap:

        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for i in arr[now]:

            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


N, M, K, X = map(int, input().split())
INF = int(1e9)
distance = [INF] * (N + 1)
arr = [[] for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    arr[a].append((b, 1))

dijkstra(X)
ans = []

for i in range(1, N + 1):
    if distance[i] == K:
        ans.append(i)

if not ans:
    print(-1)

else:
    for i in ans:
        print(i)