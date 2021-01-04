import sys

sys.setrecursionlimit(10000)


def DFS(total, pr):
    global ct

    if total == N:
        ct += 1
        return

    elif total > N:
        return

    else:
        DFS(total + pr, pr + 1)


N = int(input())
ct = 0
for i in range(1, N + 1):
    DFS(0, i)

print(ct)