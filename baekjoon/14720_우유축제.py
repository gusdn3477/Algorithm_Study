N = int(input())
arr = list(map(int, input().split()))
total = 0
first = 2

for i in arr:

    if first == 2 and i == 0:
        total += 1
        first = 0

    elif first == 0 and i == 1:
        total += 1
        first = 1

    elif first == 1 and i == 2:
        total += 1
        first = 2

print(total)