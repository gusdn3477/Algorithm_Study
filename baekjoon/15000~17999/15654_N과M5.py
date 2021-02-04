def DFS(count):
    if count == M:
        for i in answer:
            print(i, end=' ')
        print()

    for i in range(len(pocket)):
        if visited[i] == 0:
            visited[i] = 1
            answer.append(pocket[i])
            DFS(count + 1)
            visited[i] = 0
            answer.pop()


N, M = map(int, input().split())
pocket = list(map(int, input().split()))

answer = []
pocket.sort()
visited = [0] * (N + 1)
DFS(0)