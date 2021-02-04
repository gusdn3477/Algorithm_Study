arr = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
N = input()
ct = 0

for i in N:
    for j in range(len(arr)):
        if i in arr[j]:
            ct += j + 3

print(ct)