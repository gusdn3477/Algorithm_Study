N = int(input())
ct = [0] * 101
f = 0
arr = []

for i in range(N):
    a, b, c = map(int, input().split())
    arr.append((c, b, a))

arr.sort(reverse=True)

for i in range(N):
    x = arr[i][2]
    ct[x - 1] += 1

    if ct[x - 1] > 2:
        continue

    else:
        print(arr[i][2], arr[i][1])
        f += 1

    if f == 3:
        break