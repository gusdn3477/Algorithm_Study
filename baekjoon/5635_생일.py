N = int(input())
arr = []

for i in range(N):
    a, b, c, d = input().split()
    arr.append((int(d), int(c), int(b), a))

arr.sort()
print(arr[-1][3])
print(arr[0][3])