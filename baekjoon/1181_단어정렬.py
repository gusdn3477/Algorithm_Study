N = int(input())

a = []
b = []
for i in range(N):
    word = input()
    a.append(word)

a = list(set(a))

for i in range(len(a)):
    b.append((len(a[i]), a[i]))

b.sort()
for i in range(len(b)):
    print(b[i][1])