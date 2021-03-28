N = int(input())

i = 1
start = 1
total = 0

while True:

    if total + i > N:
        break

    total = total + i
    i += 1

print(i - 1)