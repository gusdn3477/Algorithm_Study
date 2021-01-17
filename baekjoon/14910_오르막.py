N = list(map(int, input().split()))
flag = 0

if len(N) == 1:
    print('Good')

else:
    for i in range(len(N) - 1):
        if N[i] > N[i + 1]:
            flag = 1
            break

    if flag == 1:
        print('Bad')

    else:
        print('Good')