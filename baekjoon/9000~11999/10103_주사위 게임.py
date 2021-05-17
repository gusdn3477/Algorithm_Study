CY = 100
SD = 100

N = int(input())

for i in range(N):
    a, b = map(int, input().split())

    if a < b:
        CY -= b

    elif a > b:
        SD -= a

print(CY)
print(SD)