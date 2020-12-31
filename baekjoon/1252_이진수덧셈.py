b = '0b'
A,B = input().split()

A = b + A
B = b + B

A = int(A, 2)
B = int(B, 2)

print(bin(A+B)[2:])