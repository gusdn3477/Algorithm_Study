import heapq


def dijkstra(start):
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:

        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for i in graph[now]:

            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


N = int(input())
M = int(input())
INF = int(1e9)
distance = [INF] * (N + 1)
graph = [[] for i in range(N + 1)]

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, destination = map(int, input().split())
dijkstra(start)
print(distance[destination])