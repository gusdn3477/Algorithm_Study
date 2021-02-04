N, M = map(int, input().split())

for i in range(1,N+1):
    if N % i == 0 and M % i == 0:
        print(i,N//i,M//i)