A, B, C = map(int, input().split())
D = int(input())

carrier = (C + D) // 60
C = (C + D) % 60

carrier2 = (B+carrier) // 60
B = (B + carrier) % 60

A = (A + carrier2) % 24

print(A,B,C)