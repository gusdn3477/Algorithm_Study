N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = list(set(A) - set(B))

if not C:
    print(0)

else:
    C.sort()
    print(len(C))
    print(*C)