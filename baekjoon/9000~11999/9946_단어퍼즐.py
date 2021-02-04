start = 1

while True:

    a = input()
    b = input()

    if a == "END" and b == "END":
        break

    a = list(a)
    b = list(b)

    a.sort()
    b.sort()

    print("Case", end=' ')
    print(start, end='')
    print(': ', end="")

    if a == b:
        print("same")

    else:
        print("different")

    start += 1