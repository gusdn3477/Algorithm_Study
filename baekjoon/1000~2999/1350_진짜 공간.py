import math

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

total = 0

for i in arr:
    total += math.ceil(i / M)

print(total * M)