a = []
for i in range(5):
    k = int(input())
    a.append(k)

b = a[0:3]
c = a[3:5]

print(min(b) + min(c) - 50)