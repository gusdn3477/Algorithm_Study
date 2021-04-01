N = int(input())

for i in range(N):
    a, b = map(list, input().split())
    a.sort()
    b.sort()

    if a == b:
        print('Possible')

    else:
        print('Impossible')