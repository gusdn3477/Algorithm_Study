N, M = map(int, input().split())
ct = 0
arr = []

for i in range(N):
    arr.append(input())

arr = {string: 0 for string in arr}

for i in range(M):
    a = input()
    if a in arr.keys():
        arr[a] += 1

b = list(arr.values())
print(sum(b))