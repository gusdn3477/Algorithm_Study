# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/901436e12d914d5e9effcd67494bbb44

import sys

def input():
    return sys.stdin.readline().rstrip()

V, E = map(int, input().split())
INF = int(1e9)
ans = INF
arr = [[INF for i in range(V)] for j in range(V)]
for i in range(E):
    a, b, c = map(int, input().split())
    arr[a-1][b-1] = c
for k in range(V):
    for i in range(V):
        for j in range(V):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
for i in range(V):
    ans = min(ans, arr[i][i])
if ans == INF:
    print(-1)
else:
    print(ans)