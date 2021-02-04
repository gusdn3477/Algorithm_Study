T = int(input())

for i in range(T):
    arr = []
    N = int(input())
    for j in range(N):
        a, b = input().split()
        arr.append((int(a), b))

    arr.sort()
    print(arr[-1][1])