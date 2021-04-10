st = ''
num = "0123456789"
n = int(input())
N = input()
arr = []

for i in N:

    if i in num:
        st += i

    elif i not in num or len(st) > 6:

        if st:
            arr.append(int(st))
            st = ''

if st:
    arr.append(int(st))

print(sum(arr))