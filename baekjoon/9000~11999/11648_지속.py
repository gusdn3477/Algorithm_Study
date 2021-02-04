N = int(input())
start = 0

while N // 10 != 0:

    a = N
    total = 1
    while a > 0:
        total *= a % 10
        a //= 10

    N = total
    start += 1

print(start)