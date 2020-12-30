a = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A, B = map(int, input().split())
poc = []

while A > 0:
    poc.append(A % B)
    A = A // B

poc = list(reversed(poc))

for i in poc:
    if i >= 10:
        print(a[i - 1], end='')

    else:
        print(i, end='')