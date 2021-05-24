N = int(input())

def moss(k):
    if k == 0:
        return 0

    elif k == 1:
        return 1

    elif k % 2 == 0:
        return moss(k // 2)

    elif k % 2 == 1:
        return 1 - moss(k // 2)


print(moss(N - 1))