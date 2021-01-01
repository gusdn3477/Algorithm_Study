N, M = map(int, input().split())
poc = []

for i in range(N):
    poc.append(input())

for i in range(N):
    for j in range(M - 1, -1, -1):
        print(poc[i][j], end='')
    print()