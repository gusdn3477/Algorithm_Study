arr = []
for i in range(9):
    arr.append(list(map(int, input().split())))

max_ = 0
for i in range(len(arr)):
    a = max(arr[i])
    if a > max_:
        max_ = a

for i in range(9):
    for j in range(9):
        if arr[i][j] == max_:
            x = i + 1
            y = j + 1
            break

print(max_)
print(x, y)