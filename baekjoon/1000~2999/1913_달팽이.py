def findAnswer(N, ans):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == ans:
                print(i + 1, j + 1)
                return


N = int(input())
arr = [[0 for i in range(N)] for j in range(N)]
ans = int(input())
start = N ** 2
x, y = -1, 0
r = N
d = 1  # 증가하는 방향
flag = 0

while start >= 1:

    for i in range(r):
        x = x + d
        arr[x][y] = start
        start -= 1

    r -= 1

    for i in range(r):
        y = y + d
        arr[x][y] = start
        start -= 1
    d = d * -1

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()

findAnswer(N, ans)