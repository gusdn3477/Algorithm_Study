arr_x = []
arr_y = []

for i in range(3):
    a, b = map(int, input().split())
    arr_x.append(a)
    arr_y.append(b)

for i in range(3):
    if arr_x.count(arr_x[i]) == 1:
        save = arr_x[i]
        break

for i in range(3):
    if arr_y.count(arr_y[i]) == 1:
        save2 = arr_y[i]
        break

print(save, save2)