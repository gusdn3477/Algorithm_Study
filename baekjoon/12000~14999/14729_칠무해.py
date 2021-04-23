from sys import stdin

arr = []
N = int(input())
for i in range(N):
    a = float(stdin.readline())
    if len(arr) < 7:
        arr.append(a)

    else:
        arr.append(a)
        arr.sort()
        arr.pop()

for i in arr:
    print('%.3f' % i)