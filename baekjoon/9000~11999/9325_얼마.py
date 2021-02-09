T = int(input())
for i in range(T):
    price = int(input())
    total = 0
    N = int(input())
    for i in range(N):
        a, b = map(int, input().split())
        total += b * a

    print(price + total)