def DFS(count, M):
    global total

    if count == M:
        total += 1
        return

    if count > M:
        return

    DFS(count + 1, M)
    DFS(count + 2, M)
    DFS(count + 3, M)


N = int(input())
poc = []
total = 0

for i in range(N):
    poc.append(int(input()))

for i in range(N):
    DFS(0, poc[i])
    print(total)
    total = 0