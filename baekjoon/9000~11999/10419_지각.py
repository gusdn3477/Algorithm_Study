N = int(input())

for i in range(N):

    a = int(input())
    MAX = 0
    for j in range(a):

        if j + j ** 2 <= a:
            MAX = j

        else:
            break

    print(MAX)