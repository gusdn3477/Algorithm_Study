N = int(input())

for _ in range(N):
    Yonsei = 0
    Korea = 0

    for i in range(9):
        a,b = map(int, input().split())
        Yonsei += a
        Korea += b

    if Yonsei < Korea:
        print('Korea')

    elif Yonsei > Korea:
        print('Yonsei')

    else:
        print('Draw')