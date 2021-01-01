N = int(input())

for i in range(N):
    st = 0
    a,b = map(int, input().split())
    for j in range(a,b+1):
        st += str(j).count('0')
    print(st)