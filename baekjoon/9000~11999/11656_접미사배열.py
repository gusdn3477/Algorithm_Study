N = input()
arr = []
b = N
for i in range(len(N)):
    arr.append(b)
    b = b[1:]

arr.sort()
for i in arr:
    print(i)