N, M = map(int, input().split())
arr = []

for i in range(M):
    a, b, c = input().split()
    arr.append((int(a), int(b), c))

arr2 = sorted(arr, key=lambda x: (x[1], x[0]))

for i in range(len(arr2)):
    print(arr2[i][2], end='')