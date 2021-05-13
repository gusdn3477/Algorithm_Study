def DFS(x, y, st):
    global M_ct

    M_ct = max(len(st), M_ct)

    for i in range(4):

        dx = x + nx[i]
        dy = y + ny[i]

        if dx < 0 or dx >= N or dy < 0 or dy >= M:
            continue

        if arr[dx][dy] in st:
            continue

        DFS(dx, dy, st + arr[dx][dy])


N, M = map(int, input().split())
arr = []
nx = [-1, 0, 1, 0]
ny = [0, 1, 0, -1]
M_ct = 0

for i in range(N):
    arr.append(input())

DFS(0, 0, arr[0][0])
print(M_ct)