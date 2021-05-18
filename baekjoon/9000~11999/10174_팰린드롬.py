N = int(input())

for i in range(N):

    a = input()
    a = a.lower()

    if a == a[::-1]:
        print('Yes')

    else:
        print('No')