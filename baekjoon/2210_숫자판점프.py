def DFS(st, x, y):
    st += arr[x][y]

    if len(st) == 6:
        poc.append(st)
        st = ''
        return

    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]

        if dx < 0 or dx >= 5 or dy < 0 or dy >= 5:
            continue

        DFS(st, dx, dy)


arr = []
poc = []
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]
st = ''
for i in range(5):
    arr.append(list(input().split()))

for i in range(5):
    for j in range(5):
        DFS(st, i, j)

print(len(set(poc)))