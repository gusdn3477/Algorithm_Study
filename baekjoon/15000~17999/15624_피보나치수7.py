N = int(input())
arr = [0] * (N + 50)
arr[1] = 1
arr[2] = 1

for i in range(3, N + 1):
    arr[i] = arr[i - 1] % 1000000007 + arr[i - 2] % 1000000007

print(arr[N] % 1000000007)