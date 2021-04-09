N, M = map(int, input().split())

arr = []
arr2 = []

for i in range(N):
    arr.append(input())

for i in range(M):
    arr2.append(input())

a = list(set(arr) & set(arr2))
a.sort()

print(len(a))
for i in a:
    print(i)