N = input()

if N == ' ':
    print('0')

else:
    N = N.lstrip()
    N = N.rstrip()
    N = N.split(' ')
    print(len(N))