for i in range(3):
    N = int(input())
    total = 0

    for j in range(N):
        a = int(input())
        total += a

    if total == 0:
        print('0')

    elif total > 0:
        print('+')

    else:
        print('-')