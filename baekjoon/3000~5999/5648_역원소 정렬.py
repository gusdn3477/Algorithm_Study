arr = []
arr2 = []
arr.extend(input().split())
N = int(arr[0])
arr.pop(0)

while True:
    arr.extend(input().split())

    if len(arr) >= N:
        break

for i in arr:
    a = i[::-1]
    arr2.append(int(a))

arr2.sort()

for i in arr2:
    print(i)