A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_count = 0
B_count = 0
win = 'D'

for i in range(len(A)):
    if A[i] > B[i]:
        A_count += 3
        win = 'A'

    elif A[i] < B[i]:
        B_count += 3
        win = 'B'

    else:
        A_count += 1
        B_count += 1

print(A_count, B_count)

if A_count > B_count:
    print('A')

elif A_count < B_count:
    print('B')

else:
    print(win)