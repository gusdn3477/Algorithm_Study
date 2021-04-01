from sys import stdin

N = int(stdin.readline())
arr = []

for i in range(N):
    arr.append(int(stdin.readline()))

arr.sort()
for i in range(N):
    print(arr[i])