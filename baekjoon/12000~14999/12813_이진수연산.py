A = input()
B = input()

for i in range(len(A)):

    if A[i] == '1' and B[i] == '1':
        print(1, end='')

    else:
        print(0, end='')

print()

for i in range(len(A)):

    if A[i] == '0' and B[i] == '0':
        print(0, end='')

    else:
        print(1, end='')

print()

for i in range(len(A)):

    if A[i] != B[i]:
        print(1, end='')

    else:
        print(0, end='')

print()

for i in range(len(A)):

    if A[i] == '1':
        print(0, end='')

    else:
        print(1, end='')

print()

for i in range(len(A)):

    if B[i] == '1':
        print(0, end='')

    else:
        print(1, end='')
