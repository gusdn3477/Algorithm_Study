a,b = map(int, input().split())
c = int(input())

b = b + c

a += b // 60
a = a % 24
b = b % 60

print(a,b)