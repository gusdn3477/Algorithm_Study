arr = [0]
A, B = map(int, input().split())

for i in range(1, 1001):
    a = [i] * i
    arr.extend(a)

    if i == B:
        break

arr = arr[A:B + 1]
print(sum(arr))