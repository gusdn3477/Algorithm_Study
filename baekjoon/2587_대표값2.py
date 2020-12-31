arr = []

for i in range(5):
    arr.append(int(input()))

print(sum(arr) // len(arr))
arr.sort()
print(arr[len(arr) // 2])