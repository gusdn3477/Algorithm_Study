jin = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
arr = []
m, n = map(int, input().split())

if m == 0:
    print(0)

while m > 0:
    remainder = m % n
    arr.append(jin[remainder])
    m = m // n

arr = list(reversed(arr))
for i in arr:
    print(i, end='')