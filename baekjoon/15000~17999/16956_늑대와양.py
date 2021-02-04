def DFS(x, y):
    global flag

    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]

        if dx < 0 or dx > N - 1 or dy < 0 or dy > M - 1:
            continue

        if arr[dx][dy] == '.':
            arr[dx][dy] = 'D'

        elif arr[dx][dy] == 'S':
            continue

        elif arr[dx][dy] == 'W':
            flag = 1
            return


N, M = map(int, input().split())
arr = []
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]
flag = 0
for i in range(N):
    arr.append(list(input()))

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'S':
            DFS(i, j)

if flag == 1:
    print(0)

else:
    print(1)
    for i in range(N):
        for j in range(M):
            print(arr[i][j], end='')
        print()