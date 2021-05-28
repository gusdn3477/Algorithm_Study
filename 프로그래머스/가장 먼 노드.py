from collections import deque

def solution(n, edge):
    answer = 0
    distance = [0] * (n + 1)
    graph = [[] for i in range(n + 1)]
    visited = [0] * (n + 1)

    for i in range(len(edge)):
        graph[edge[i][0]].append(edge[i][1])
        graph[edge[i][1]].append(edge[i][0])

    queue = deque()
    queue.append((1, 0))
    visited[1] = 1

    while queue:

        a = queue.popleft()

        for i in graph[a[0]]:
            if distance[i] == 0 and visited[i] == 0:
                visited[i] = 1
                distance[i] = a[1] + 1
                queue.append((i, a[1] + 1))

    print(distance)
    return distance.count(max(distance))