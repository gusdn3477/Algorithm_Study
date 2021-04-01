st = input()
s = []

for i in range(len(st)):
    t = st[i]
    for j in range(i + 1, len(st)):

        if t:
            s.append(t)

        t += st[j]

    if t:
        s.append(t)

print(len(set(s)))