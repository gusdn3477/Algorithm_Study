N = int(input())
a = 2 ** N
total = (a - 1) * a // 2

print(bin(total)[2:])