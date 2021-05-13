arr = []
arr2 = []

for i in range(20):

    a = int(input())

    if i < 10:
        arr.append(a)

    else:
        arr2.append(a)

arr.sort(reverse=True)
arr2.sort(reverse=True)
t = arr[0] + arr[1] + arr[2]
t2 = arr2[0] + arr2[1] + arr2[2]

print(t, t2)