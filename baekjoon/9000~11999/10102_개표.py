N = int(input())
A_ct = 0
B_ct = 0

a = input()

for i in a:

    if i == 'A':
        A_ct += 1

    if i == 'B':
        B_ct += 1

if A_ct == B_ct:
    print('Tie')

elif A_ct > B_ct:
    print('A')

else:
    print('B')