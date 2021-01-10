gandalf = [1, 2, 3, 3, 4, 10]
sauron = [1, 2, 2, 2, 3, 5, 10]

N = int(input())

for i in range(1, N + 1):

    arr = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    team1 = 0
    team2 = 0

    for j in range(len(arr)):
        team1 += (gandalf[j] * arr[j])

    for j in range(len(arr2)):
        team2 += (sauron[j] * arr2[j])

    print('Battle', i, end='')

    if team1 == team2:
        print(': No victor on this battle field')

    elif team1 > team2:
        print(': Good triumphs over Evil')

    else:
        print(': Evil eradicates all trace of Good')