N = input()
M = input()
ct = 0

while True:

    a = N.find(M)
    if a == -1:
        break

    ct += 1
    N = N[a + len(M):]

print(ct)