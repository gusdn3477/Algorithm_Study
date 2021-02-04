from itertools import permutations

N = int(input())

for i in range(N):
    arr = []
    flag = 0
    M = int(input())

    for j in range(M):
        arr.append(input())

    a = list(permutations(arr, 2))

    for k in range(len(a)):
        st = ""
        st = a[k][0] + a[k][1]
        st2 = st[::-1]

        if st == st2:
            flag = 1
            print(st)
            break

    if flag == 0:
        print(0)