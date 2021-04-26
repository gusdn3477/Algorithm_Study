alphabet = "abcdefghijklmnopqrstuvwxyz"

while True:

    dic = {}
    a = input()

    if a == '#':
        break

    a = a.lower()
    for i in a:

        if i not in alphabet:
            continue

        if i not in dic:
            dic[i] = 1


    arr = list(dic.values())
    print(sum(arr))