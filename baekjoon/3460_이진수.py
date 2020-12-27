N = int(input())

for i in range(N):
    A = int(input())
    A = bin(A)[2:]

    A = A[::-1]

    for i in range(len(A)):
        if A[i] == '1':
            print(i, end=' ')