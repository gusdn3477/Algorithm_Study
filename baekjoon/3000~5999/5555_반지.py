st = input()
N = int(input())
arr = []
ct = 0

for i in range(N):
    para = input()
    para = para + para
    arr.append(para)

for i in range(N):
    if st in arr[i]:
        ct += 1

print(ct)