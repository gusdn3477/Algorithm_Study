N = int(input())

for i in range(1, N + 1):
    # 공백 출력
    for j in range(N - i):
        print(' ', end='')

    # 별 출력 후 개행
    for j in range(i * 2 - 1):
        print('*', end='')
    print()

for i in range(1, N + 1):
    # 공백 출력
    for j in range(i):
        print(' ', end='')

    # 별 출력 후 개행
    for j in range((N - i - 1) * 2 + 1):
        print('*', end='')
    print()