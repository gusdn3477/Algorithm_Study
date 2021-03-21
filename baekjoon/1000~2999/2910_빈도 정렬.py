N, C = map(int, input().split())
dic = {}
arr = list(map(int, input().split()))

for i in arr:
    if i not in dic:
        dic[i] = 1

    else:
        dic[i] += 1

a = list(dic.items())
a = sorted(a, key=lambda x: x[1], reverse=True)

for i in range(len(a)):

    b = a[i][1]
    for j in range(b):
        print(a[i][0], end=' ')