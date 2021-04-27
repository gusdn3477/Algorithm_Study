from sys import stdin

N = int(input())
dic = {}
arr = []
total = 0
for i in range(N):

    a = int(input())
    arr.append(a)
    if a not in dic:
        dic[a] = 1

    else:
        dic[a] += 1

dic = dic.items()
arr2 = sorted(dic, key=lambda x: (-x[1], x[0]))
a = arr2[0]

if len(dic) > 1:
    if a[1] == arr2[1][1]:
        a = arr2[1]

arr.sort()

if sum(arr) >= 0:
    b = int((sum(arr) / N) + 0.5)

else:
    b = int((sum(arr) / N) - 0.5)

print(b)
print(arr[len(arr) // 2])
print(a[0])
print(arr[-1] - arr[0])