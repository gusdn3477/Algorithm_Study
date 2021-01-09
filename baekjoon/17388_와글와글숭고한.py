A, B, C = map(int, input().split())

if A + B + C >= 100:
    print('OK')

else:
    if A == min(A, B, C):
        print('Soongsil')

    elif B == min(A, B, C):
        print('Korea')

    else:
        print('Hanyang')