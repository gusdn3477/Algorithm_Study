T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    total = 0

    for i in arr:
        total += i // K

    print(total)