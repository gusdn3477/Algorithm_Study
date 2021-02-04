A, P = map(int, input().split())
arr = [A]
while True:

    save = arr[-1]
    temp = 0
    while save > 0:
        temp += ((save % 10) ** P)
        save = save // 10

    if temp in arr:
        break

    arr.append(temp)

idx = arr.index(temp)
arr = arr[:idx]
print(len(arr))