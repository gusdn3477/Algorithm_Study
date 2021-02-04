N = int(input())

for i in range(N):
    A,B = input().split()
    A = int(A)
    C = B[0:A-1]
    C +=B[A:]
    print(C)