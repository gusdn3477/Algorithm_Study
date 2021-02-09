N = int(input())
arr = {}

for i in range(N):
    a, b = input().split()

    if a not in arr:
        arr[a] = 1

    if a in arr and b == "leave":
        del arr[a]

sdict = sorted(arr, reverse=True)

for i in sdict:
    print(i)