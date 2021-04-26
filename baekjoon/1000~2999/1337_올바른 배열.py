N = int(input())
arr = []
ct = 0
tmp = 0

for i in range(N):
    arr.append(int(input()))

arr.sort()
for i in range(N):
    tmp = 0
    for j in range(5):
        if arr[i] + j in arr:
            tmp += 1

    ct = max(ct, tmp)

a = 5 - ct

if a < 0:
    print(0)

else:
    print(a)