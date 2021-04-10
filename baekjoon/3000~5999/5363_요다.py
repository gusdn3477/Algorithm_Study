N = int(input())
for i in range(N):
    a = input().split()
    for j in range(2, len(a)):
        print(a[j], end=' ')

    for j in range(2):
        print(a[j], end=' ')