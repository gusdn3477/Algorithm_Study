from sys import stdin

N = int(input())

arr = []
start = 1

for i in range(32):
    arr.append(start)
    start *= 2

for i in range(N):

    a = int(stdin.readline())

    if a in arr:
        print(1)

    else:
        print(0)