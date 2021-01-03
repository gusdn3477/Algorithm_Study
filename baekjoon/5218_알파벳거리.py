N = int(input())

for i in range(N):

    a, b = input().split()
    print('Distances: ', end='')
    for i in range(len(a)):
        x = ord(a[i])
        y = ord(b[i])
        if x > y:
            print(y + 26 - x, end=' ')

        else:
            print(y - x, end=' ')
    print()