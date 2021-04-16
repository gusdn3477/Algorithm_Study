N = int(input())

a = bin(N)[2:]
a = a[::-1]
print(int(a,2))