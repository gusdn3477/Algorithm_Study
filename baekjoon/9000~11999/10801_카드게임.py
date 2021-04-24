arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

ct = 0
ct2 = 0

for i in range(len(arr)):

    if arr[i] > arr2[i]:
        ct += 1

    elif arr[i] < arr2[i]:
        ct2 += 1

if ct > ct2:
    print('A')

elif ct < ct2:
    print('B')

else:
    print('D')