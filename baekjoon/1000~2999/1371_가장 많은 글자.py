dic = {}

while True:

    try:
        a = input()
        for i in a:

            if i == ' ':
                continue

            if i not in dic:
                dic[i] = 1

            else:
                dic[i] += 1

    except:
        break

ar = list(dic.items())
ar = sorted(ar, key=lambda x: (-x[1], x[0]))
M = ar[0][1]

for i in range(len(ar)):
    if ar[i][1] == M:
        print(ar[i][0], end='')