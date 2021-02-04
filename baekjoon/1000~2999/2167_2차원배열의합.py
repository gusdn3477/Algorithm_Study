N, M = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))

K = int(input())

for m in range(K):
    total = 0
    i, j, x, y = map(int, input().split())
    for a in range(j - 1, y):
        for b in range(i - 1, x):
            total += graph[b][a]

    print(total)