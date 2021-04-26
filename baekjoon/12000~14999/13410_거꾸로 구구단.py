N, M = map(int, input().split())

arr = []

for i in range(1, M + 1):
    a = str(N * i)
    a = a[::-1]
    arr.append(int(a))

print(max(arr))