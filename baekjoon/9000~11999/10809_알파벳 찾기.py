dic = {}

for i in range(26):
    dic[chr(ord('a')+i)] = -1

a = input()

for i in a:
    if dic[i] != -1:
        continue

    else:
        dic[i] = a.find(i)

for i in dic.values():
    print(i,end=' ')