import heapq


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:

        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for i in graph[now]:

            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


V, E = map(int, input().split())
start = int(input())

INF = int(1e9)
distance = [INF] * (V + 1)
graph = [[] for i in range(V + 1)]

for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(start)

for i in range(1, V + 1):

    if distance[i] == INF:
        print('INF')

    else:
        print(distance[i])