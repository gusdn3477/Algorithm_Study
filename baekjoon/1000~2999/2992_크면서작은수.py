from itertools import permutations

N = input()

arr = []
a = list(permutations(N, len(N)))
a = list(set(a))
a.sort()

for i in range(len(a)):
    st = ''
    for j in range(len(a[i])):
        st += a[i][j]

    arr.append(int(st))

b = arr.index(int(N))
c = b + 1
if c < len(arr):
    print(arr[c])

else:
    print(0)