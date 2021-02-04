N = int(input())
start = 0
arr = []

for i in range(N):
    arr.append(input())

a = arr[0]
ct = 0
length = 0

for i in range(len(a)):
    ct = 0
    for j in range(len(arr)):
        if arr[j][i] == a[i]:
            ct += 1

    if ct == N:
        print(a[i], end='')

    else:
        print('?', end='')