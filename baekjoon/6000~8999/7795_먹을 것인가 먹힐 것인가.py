from bisect import bisect_left

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    total = 0

    for i in A:
        total += bisect_left(B, i)

    print(total)