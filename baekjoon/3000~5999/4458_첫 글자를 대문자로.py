N = int(input())

for i in range(N):
    a = input().split(' ')

    for j in range(len(a)):
        st = ''

        if j == 0:
            st += a[j][0].upper() + a[j][1:]

        else:
            st += a[j]
        print(st, end=' ')
    print()