N, a, b = map(int, input().split())
ct = 1

if a < b:
    while a < b:

        if a % 2 != 0 and b % 2 == 0 and b-a == 1:
            break

        ct += 1

        a = (a+1) // 2
        b = (b+1) // 2

else:
    while b < a:

        if b % 2 != 0 and a % 2 == 0 and a-b == 1:
            break

        ct += 1

        a = (a+1) // 2
        b = (b+1) // 2

print(ct)