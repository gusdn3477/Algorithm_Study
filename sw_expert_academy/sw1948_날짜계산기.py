def returnday(month):
    total = 0
    for j in range(0, month):
        total += day[j]

    return total


N = int(input())
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, N + 1):
    a, b, c, d = map(int, input().split())
    days = returnday(a - 1) + b
    days2 = returnday(c - 1) + d
    print('#' + str(i), days2 - days + 1)