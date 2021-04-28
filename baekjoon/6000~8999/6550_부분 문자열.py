while True:

    try:

        a, b = input().split()
        flag = 1

        for i in range(len(a)):
            if a[i] in b:
                idx = b.find(a[i])
                b = b[idx + 1:]

            else:
                flag = 0
                break

        if flag:
            print('Yes')

        else:
            print('No')

    except:
        break