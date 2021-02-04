N = int(input())

for i in range(N):
    st = 'god'
    a = input().split()
    for i in range(1,len(a)):
        st += a[i]
    print(st)