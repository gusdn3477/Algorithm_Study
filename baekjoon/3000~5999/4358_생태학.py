from sys import stdin

dic = {}

while True:

    try:
        a = input()

        if a in dic:
            dic[a] += 1

        else:
            dic[a] = 1

    except:
        break

arr = list(dic.items())
arr.sort()
total = sum(dic.values())

for i in range(len(arr)):
    k = arr[i][1] / total * 100
    k += 0.00005
    k = str(k)
    idx = k.find('.')
    k = k[:idx + 5]
    print(arr[i][0], k)