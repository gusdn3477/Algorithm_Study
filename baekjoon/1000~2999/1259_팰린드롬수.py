while True:

    N = input()
    if N == '0':
        break

    b = N[::-1]
    if N == b:
        print('yes')

    else:
        print('no')