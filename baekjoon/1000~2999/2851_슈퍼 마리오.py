arr = []
total = 0
a, b = 0, 0

for i in range(10):
    arr.append(int(input()))

for i in range(10):

    if total + arr[i] > 100:
        a = total
        b = total + arr[i]
        break

    total += arr[i]

if a == 0:
    print(total)

else:
    if abs(100 - a) == abs(100 - b):
        print(b)

    elif abs(100 - a) > abs(100 - b):
        print(b)

    else:
        print(a)