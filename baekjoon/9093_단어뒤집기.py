N = int(input())
for i in range(N):
    st = input().split()
    for j in range(len(st)):
        print(st[j][::-1], end=' ')
    print()