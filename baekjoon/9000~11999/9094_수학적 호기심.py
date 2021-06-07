N = int(input())
arr = []

for i in range(N):
    n, m = map(int, input().split())
    ct = 0
    for i in range(1,n):
        for j in range(i+1,n):
            if (i * i + j * j + m) // (i * j) == (i * i + j * j + m) / (i * j):
                ct += 1
                
    print(ct)