A, B = list(map(int, input().split()))

arr = []
arr2 = []

while A:
    arr.append(A % 10)
    A //= 10

while B:
    arr2.append(B % 10)
    B //= 10

arr.sort()
arr2.sort()

total = 0
for i in arr:
    for j in arr2:
        total += i * j

print(total)