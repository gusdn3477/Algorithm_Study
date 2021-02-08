arr = []
flag = 0

for i in range(5):
    arr.append(input())

for i in range(5):
    if 'FBI' in arr[i]:
        flag = 1
        print(i + 1, end=' ')

if flag == 0:
    print('HE GOT AWAY!')