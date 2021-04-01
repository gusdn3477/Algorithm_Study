N, K = map(int, input().split())
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

arr = sorted(arr, key=lambda x: (x[1], x[2], x[3]), reverse=True)

arr[0].append(1)

for i in range(1, N):

    if arr[i][1] == arr[i - 1][1] and arr[i][2] == arr[i - 1][2] and arr[i][3] == arr[i - 1][3]:
        arr[i].append(arr[i - 1][4])

    else:
        arr[i].append(i + 1)

for i in range(N):
    if arr[i][0] == K:
        print(arr[i][4])
        break