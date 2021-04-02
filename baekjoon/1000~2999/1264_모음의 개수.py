ar = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:

    a = input()
    ct = 0
    if a == '#':
        break

    for i in ar:
        ct += a.count(i)

    print(ct)