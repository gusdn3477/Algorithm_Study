a = input()
idx = 0
flag = 0

while True:

    if not a:
        flag = 1
        break

    if a[:2] == 'pi':
        idx = a.find('pi') + 2

    elif a[:2] == 'ka':
        idx = a.find('ka') + 2

    elif a[:3] == 'chu':
        idx = a.find('chu') + 3

    else:
        break

    a = a[idx:]

if flag:
    print('YES')

else:
    print('NO')