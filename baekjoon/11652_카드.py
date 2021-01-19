N = int(input())
a = dict()
m = 0
n = 0
for i in range(N):
    x = int(input())

    if x in a.keys():
        a[x] += 1

    else:
        a[x] = 1

sdict = sorted(a.items())

for i, j in sdict:
    if j > m:
        n, m = i, j

print(n)