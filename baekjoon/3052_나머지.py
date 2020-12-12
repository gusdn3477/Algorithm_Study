a = []
for i in range(10):
    x = int(input())
    a.append(x % 42)

a = set(a)
print(len(a))