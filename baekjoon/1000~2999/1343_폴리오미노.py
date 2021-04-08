def check(N):
    for i in N:
        if i == 'X':
            return False

    return True


N = input()

N = N.replace('XXXX', 'AAAA')
N = N.replace('XX', 'BB')

if check(N):
    print(N)

else:
    print(-1)