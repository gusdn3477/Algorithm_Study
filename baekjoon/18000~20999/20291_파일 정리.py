N = int(input())
dic = {}

for i in range(N):
    a = input()
    idx = a.find('.')
    b = a[idx + 1:]

    if b in dic:
        dic[b] += 1

    else:
        dic[b] = 1

k = list(dic.items())
k.sort()
for i, j in k:
    print(i, j)