N = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

total = 0
a.sort(reverse=True)
b.sort()

for i in range(len(a)):
    total += a[i] * b[i]

print(total)