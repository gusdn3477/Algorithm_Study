# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/901436e12d914d5e9effcd67494bbb44

import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for i in range(T):
    n = int(input())
    arr = []
    for j in range(2):
        arr.append(list(map(int, input().split())))
    if n == 1:
        print(max(arr[0][0], arr[1][0]))
    else:
        arr[0][1] = arr[1][0] + arr[0][1]
        arr[1][1] = arr[1][1] + arr[0][0]
        for j in range(2, n):
            arr[0][j] += max(arr[1][j-1], arr[1][j-2])
            arr[1][j] += max(arr[0][j-1], arr[0][j-2])
        print(max(arr[0][-1], arr[1][-1]))