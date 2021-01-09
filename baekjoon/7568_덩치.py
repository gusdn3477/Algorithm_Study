N = int(input())
arr = []

for i in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

for i in range(N):
    start = 1
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            start += 1

    print(start, end=' ')