N = int(input())
arr = list(map(int, input().split()))

for i in range(N):
    total = 0
    for j in range(1, arr[i]):
        if arr[i] % j == 0:
            total += j

    if total == arr[i]:
        print('Perfect')

    elif total < arr[i]:
        print('Deficient')

    else:
        print('Abundant')