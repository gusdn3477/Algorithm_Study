N = int(input())

for i in range(N):
    b = int(input())
    a = list(map(int, input().split()))
    print(sum(a))