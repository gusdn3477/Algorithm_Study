def back(x, y, st):
    if y == N:
        arr.append(st)
        return

    for i in range(x, 4):
        st += dic[ans[i]]
        back(i, y + 1, st)
        st -= dic[ans[i]]


dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
st = 0
ans = 'IVXL'
arr = []
N = int(input())
back(0, 0, 0)
print(len(set(arr)))