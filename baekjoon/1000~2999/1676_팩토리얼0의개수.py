N = int(input())
a = 1
ct = 0

for i in range(N, 0, -1):
    a *= i

a = str(a)
for i in range(len(a) - 1, -1, -1):
    if a[i] == '0':
        ct += 1

    else:
        break

print(ct)